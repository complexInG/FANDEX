# C++ 序列化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## JSON 序列化

**基本写法：nlohmann/json**
`#include <nlohmann/json.hpp>`
```cpp
#include <nlohmann/json.hpp>
using json = nlohmann::json;
// 构造 JSON
json j;
j["name"] = "Alice";
j["age"] = 30;
j["scores"] = {90, 85, 92};
std::string s = j.dump();        // 序列化为字符串
std::string p = j.dump(4);       // 格式化缩进 4 空格
```

---

**基本写法：解析 JSON**
`json::parse(<字符串>)`
```cpp
// 从字符串解析
json j = json::parse(R"({"name":"Bob","age":25})");
std::string name = j["name"];
int age = j["age"];
// 从文件解析
std::ifstream f("data.json");
json jf = json::parse(f);
```

---

**基本写法：结构体与 JSON 互转**
`NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE`
```cpp
struct Person {
    std::string name;
    int age;
};
NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(Person, name, age)
// 自动生成 to_json / from_json
Person p{"Alice", 30};
json j = p;                   // 结构体转 JSON
Person p2 = j.get<Person>();  // JSON 转结构体
```

---

## 二进制序列化

**基本写法：手写二进制**
`<流>.write(<指针>, <大小>)`
```cpp
#include <fstream>
// 写入二进制
struct Header {
    uint32_t magic;
    uint32_t version;
    uint64_t size;
};
std::ofstream out("data.bin", std::ios::binary);
Header h{0x4D4946, 1, 1024};
out.write(reinterpret_cast<const char*>(&h), sizeof(h));
// 读取
std::ifstream in("data.bin", std::ios::binary);
Header h2;
in.read(reinterpret_cast<char*>(&h2), sizeof(h2));
```

---

**基本写法：字节序处理**
`std::endian` `htobe32` 等
```cpp
#include <bit>
#include <endian.h>
// C++20 检查字节序
if constexpr (std::endian::native == std::endian::little) {
    // 小端
}
// 转网络字节序（大端）
uint32_t net = htobe32(local_value);
uint32_t local = be32toh(net);
```

---

## Protobuf

**基本写法：定义消息**
`message <名> { <字段>; }`
```protobuf
// person.proto
syntax = "proto3";
message Person {
    string name = 1;
    int32 age = 2;
    repeated string emails = 3;
}
```

---

**基本写法：使用 Protobuf**
`<消息>.SerializeToString(<串>)`
```cpp
#include "person.pb.h"
// 序列化
Person p;
p.set_name("Alice");
p.set_age(30);
p.add_emails("alice@example.com");
std::string output;
p.SerializeToString(&output);
// 反序列化
Person p2;
p2.ParseFromString(output);
std::cout << p2.name();
```

---

## Cereal 库

**基本写法：cereal 序列化**
`cereal::JSONOutputArchive`
```cpp
#include <cereal/cereal.hpp>
#include <cereal/archives/json.hpp>
#include <fstream>
struct Data {
    int x;
    std::string y;
    template <typename Archive>
    void serialize(Archive& ar) {
        ar(x, y);
    }
};
// 序列化
std::ofstream os("data.json");
cereal::JSONOutputArchive ar(os);
Data d{42, "hello"};
ar(d);
```

---

## 流式序列化

**基本写法：operator<<**
`std::ostream& operator<<(std::ostream&, <类型>)`
```cpp
// 自定义输出
struct Point { int x, y; };
std::ostream& operator<<(std::ostream& os, const Point& p) {
    return os << "(" << p.x << "," << p.y << ")";
}
Point p{3, 4};
std::cout << p; // (3,4)
std::stringstream ss;
ss << p; // 序列化到字符串
```

---

**基本写法：operator>>**
`std::istream& operator>>(std::istream&, <类型>&)`
```cpp
// 自定义输入
std::istream& operator>>(std::istream& is, Point& p) {
    char c;
    return is >> c >> p.x >> c >> p.y >> c; // (3,4)
}
std::stringstream ss("(3,4)");
Point p;
ss >> p; // 反序列化
```

---

## 网络字节序

**基本写法：htonl/ntohl**
`htonl(<32位>)` `ntohl(<32位>)`
```cpp
#include <arpa/inet.h>
// 主机字节序转网络字节序
uint32_t host = 0x12345678;
uint32_t net = htonl(host);
uint32_t back = ntohl(net);
// 16 位
uint16_t net16 = htons(8080);
uint16_t host16 = ntohs(net16);
```

---

## 版本兼容

**基本写法：版本号字段**
`struct <数据> { uint32_t version; ... };`
```cpp
// 序列化时记录版本
struct Data {
    uint32_t version = 1;
    int x;
    std::string y;
    // 版本 2 新增字段
    // double z = 0; // 旧版本无此字段
};
// 读取时根据版本决定如何解析
```
