# Java 网络编程 API 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Socket TCP 客户端

**基本写法：创建客户端连接**
`new Socket(<host>, <port>)`
```java
// 建立与服务端的 TCP 连接
try (Socket socket = new Socket("example.com", 8080)) {
    OutputStream out = socket.getOutputStream();
    out.write("hello".getBytes());
}
```

---

**基本写法：读取服务端响应**
`<socket>.getInputStream()`
```java
// 从输入流读取服务端返回数据
try (Socket socket = new Socket("example.com", 8080);
     BufferedReader reader = new BufferedReader(
         new InputStreamReader(socket.getInputStream()))) {
    String line = reader.readLine();
}
```

---

**基本写法：设置超时**
`<socket>.setSoTimeout(<ms>)`
```java
// 读操作最长等待时间
Socket socket = new Socket("example.com", 8080);
socket.setSoTimeout(5000);
```

---

**基本写法：连接超时**
`new Socket()` + `<socket>.connect(<endpoint>, <timeout>)`
```java
// 控制连接建立阶段超时
Socket socket = new Socket();
socket.connect(new InetSocketAddress("example.com", 8080), 3000);
```

---

## Socket TCP 服务端

**基本写法：创建服务端**
`new ServerSocket(<port>)`
```java
// 监听指定端口
try (ServerSocket server = new ServerSocket(8080)) {
    Socket client = server.accept();
    handleClient(client);
}
```

---

**基本写法：循环接收连接**
`while (true) { <server>.accept(); }`
```java
// 持续接收客户端连接
try (ServerSocket server = new ServerSocket(8080)) {
    while (true) {
        Socket client = server.accept();
        new Thread(() -> handleClient(client)).start();
    }
}
```

---

**基本写法：设置接收缓冲区**
`<server>.setReceiveBufferSize(<size>)`
```java
// 调整服务端接收缓冲区大小
ServerSocket server = new ServerSocket(8080);
server.setReceiveBufferSize(64 * 1024);
```

---

## UDP 数据报

**基本写法：发送 UDP 包**
`new DatagramSocket()` + `<socket>.send(<packet>)`
```java
// 发送数据报到目标地址
try (DatagramSocket socket = new DatagramSocket()) {
    byte[] data = "hello".getBytes();
    DatagramPacket packet = new DatagramPacket(
        data, data.length, InetAddress.getByName("127.0.0.1"), 9090);
    socket.send(packet);
}
```

---

**基本写法：接收 UDP 包**
`new DatagramSocket(<port>)` + `<socket>.receive(<packet>)`
```java
// 在指定端口监听 UDP 数据报
try (DatagramSocket socket = new DatagramSocket(9090)) {
    byte[] buffer = new byte[1024];
    DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
    socket.receive(packet);
    String msg = new String(packet.getData(), 0, packet.getLength());
}
```

---

## URL 访问

**基本写法：打开 URL 连接**
`new URL(<url>).openConnection()`
```java
// 传统 URL 读取方式
URL url = new URL("https://example.com/api");
try (BufferedReader reader = new BufferedReader(
        new InputStreamReader(url.openStream()))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
}
```

---

**基本写法：HTTP GET 请求**
`<conn>.setRequestMethod("GET")`
```java
// 通过 HttpURLConnection 发送 GET
URL url = new URL("https://example.com/api");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("GET");
conn.setRequestProperty("Accept", "application/json");
int code = conn.getResponseCode();
```

---

**基本写法：HTTP POST 请求**
`<conn>.setRequestMethod("POST")` + `<conn>.getOutputStream()`
```java
// 发送 POST 请求并写入请求体
HttpURLConnection conn = (HttpURLConnection) new URL("https://example.com/api").openConnection();
conn.setRequestMethod("POST");
conn.setDoOutput(true);
conn.setRequestProperty("Content-Type", "application/json");
try (OutputStream os = conn.getOutputStream()) {
    os.write("{\"name\":\"Alice\"}".getBytes());
}
```

---

## HttpClient（Java 11+）

**基本写法：创建 HttpClient**
`HttpClient.newHttpClient()`
```java
// 创建默认 HTTP 客户端
HttpClient client = HttpClient.newHttpClient();
```

---

**基本写法：自定义 HttpClient**
`HttpClient.newBuilder()`
```java
// 配置连接超时、HTTP 版本等
HttpClient client = HttpClient.newBuilder()
    .version(HttpClient.Version.HTTP_2)
    .connectTimeout(Duration.ofSeconds(10))
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();
```

---

**基本写法：发送 GET 请求**
`<client>.send(<request>, <handler>)`
```java
// 同步发送 GET 并返回响应
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api"))
    .timeout(Duration.ofSeconds(10))
    .header("Accept", "application/json")
    .GET()
    .build();
HttpResponse<String> response =
    client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

---

**基本写法：发送 POST 请求**
`HttpRequest.BodyPublishers.ofString(<body>)`
```java
// 发送 JSON 请求体
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api"))
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString("{\"name\":\"Alice\"}"))
    .build();
HttpResponse<String> response =
    client.send(request, HttpResponse.BodyHandlers.ofString());
```

---

**基本写法：异步发送请求**
`<client>.sendAsync(<request>, <handler>)`
```java
// 返回 CompletableFuture，非阻塞
client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
    .thenApply(HttpResponse::body)
    .thenAccept(System.out::println);
```

---

**基本写法：发送 PUT 请求**
`.PUT(HttpRequest.BodyPublishers.ofString(<body>))`
```java
// RESTful PUT 请求
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api/1"))
    .header("Content-Type", "application/json")
    .PUT(HttpRequest.BodyPublishers.ofString("{\"name\":\"Bob\"}"))
    .build();
```

---

**基本写法：发送 DELETE 请求**
`.DELETE()`
```java
// RESTful DELETE 请求
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api/1"))
    .DELETE()
    .build();
```

---

**基本写法：处理响应体为字节数组**
`HttpResponse.BodyHandlers.ofByteArray()`
```java
// 适用于下载二进制文件
HttpResponse<byte[]> response =
    client.send(request, HttpResponse.BodyHandlers.ofByteArray());
Files.write(Path.of("out.bin"), response.body());
```

---

**基本写法：流式处理响应体**
`HttpResponse.BodyHandlers.ofInputStream()`
```java
// 大响应体流式读取
HttpResponse<InputStream> response =
    client.send(request, HttpResponse.BodyHandlers.ofInputStream());
try (InputStream is = response.body()) {
    is.transferTo(System.out);
}
```

---

## 基本参数与查询

**基本写法：拼接查询参数**
`URI.create(<url> + "?" + <query>)`
```java
// 手动拼接 URL 查询参数
String url = "https://example.com/search?q=" + URLEncoder.encode("Java 编程", StandardCharsets.UTF_8);
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(url))
    .GET()
    .build();
```

---

**基本写法：设置 Basic 认证**
`<builder>.header("Authorization", "Basic " + <encoded>)`
```java
// 用户名密码 Basic 认证
String auth = "alice:secret";
String encoded = Base64.getEncoder().encodeToString(auth.getBytes());
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api"))
    .header("Authorization", "Basic " + encoded)
    .GET()
    .build();
```

---

## InetSocketAddress 地址

**基本写法：创建地址对象**
`new InetSocketAddress(<host>, <port>)`
```java
// 封装主机名与端口
InetSocketAddress addr = new InetSocketAddress("example.com", 8080);
```

---

**基本写法：未解析地址**
`InetSocketAddress.createUnresolved(<host>, <port>)`
```java
// 不进行 DNS 解析，连接时才解析
InetSocketAddress addr = InetSocketAddress.createUnresolved("example.com", 8080);
```

---

## NetworkInterface 网络接口

**基本写法：列举所有网卡**
`NetworkInterface.getNetworkInterfaces()`
```java
// 遍历本机所有网络接口
Enumeration<NetworkInterface> nics = NetworkInterface.getNetworkInterfaces();
while (nics.hasMoreElements()) {
    NetworkInterface nic = nics.nextElement();
    System.out.println(nic.getName());
}
```

---

**基本写法：获取本机 IP**
`NetworkInterface.getByName(<name>)`
```java
// 通过网卡名获取其 IP 地址
NetworkInterface nic = NetworkInterface.getByName("eth0");
Enumeration<InetAddress> addrs = nic.getInetAddresses();
while (addrs.hasMoreElements()) {
    System.out.println(addrs.nextElement().getHostAddress());
}
```

---

## ServerSocket 多线程处理

**基本写法：线程池处理客户端**
`ExecutorService` + `server.accept()`
```java
// 使用线程池避免无限创建线程
ExecutorService pool = Executors.newFixedThreadPool(50);
try (ServerSocket server = new ServerSocket(8080)) {
    while (true) {
        Socket client = server.accept();
        pool.submit(() -> handleClient(client));
    }
}
```

---

**基本写法：NIO Selector 监听**
`Selector.open()`
```java
// 单线程管理多通道，适合高并发
Selector selector = Selector.open();
ServerSocketChannel server = ServerSocketChannel.open();
server.configureBlocking(false);
server.register(selector, SelectionKey.OP_ACCEPT);
```

---

## 文件传输

**基本写法：服务端发送文件**
`Files.copy(<path>, <outputStream>)`
```java
// 将文件写入 Socket 输出流
try (Socket socket = server.accept();
     OutputStream out = socket.getOutputStream()) {
    Files.copy(Path.of("data.txt"), out);
}
```

---

**基本写法：客户端接收文件**
`<inputStream>.transferTo(<outputStream>)`
```java
// 接收服务端传输的文件内容
try (InputStream in = socket.getInputStream();
     FileOutputStream fos = new FileOutputStream("received.txt")) {
    in.transferTo(fos);
}
```
