---
order: 200
title: 地理位置定位
module: 'html5'
category: 前端技术
difficulty: intermediate
description: Geolocation
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/018-WebComponentsPWADevelopment'
  - 'html5/019-DragAPI'
  - 'html5/022-ServiceWorkerPWA'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：地图、外卖、打卡都靠它

外卖 App 显示“距你 1.2 公里”，地图定位到你的实时位置，社交软件分享“我在哪”——这些功能都来自 Geolocation API。

它不是 GPS 本身，而是浏览器向系统（GPS、Wi-Fi、基站）申请位置的统一接口。使用时注意：浏览器会弹出授权询问，用户拒绝后无法强行获取；网页只能拿到“经纬度 + 精度”，拿不到精确地址，地址需要靠地图服务反查。

## 1. Geolocation API

```javascript
if ('geolocation' in navigator) {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      console.log('纬度:', position.coords.latitude);
      console.log('经度:', position.coords.longitude);
      console.log('精度:', position.coords.accuracy);
    },
    (error) => {
      switch (error.code) {
        case error.PERMISSION_DENIED:
          console.error('用户拒绝');
          break;
        case error.POSITION_UNAVAILABLE:
          console.error('位置不可用');
          break;
        case error.TIMEOUT:
          console.error('请求超时');
          break;
      }
    },
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
  );
}
```

**讲解：**

- 先判断 `'geolocation' in navigator`，不支持的环境直接提示；
- `getCurrentPosition` 接收成功、失败两个回调，以及可选的配置；
- 错误码三种：拒绝授权、位置不可用、请求超时；
- `enableHighAccuracy` 请求高精度（更耗电），`timeout` 是超时，`maximumAge` 允许复用缓存。

### watchPosition

```javascript
const watchId = navigator.geolocation.watchPosition(
  (pos) => console.log(`位置: ${pos.coords.latitude}, ${pos.coords.longitude}`),
  (err) => console.error(err),
  { enableHighAccuracy: true }
);
navigator.geolocation.clearWatch(watchId);
```

**讲解：**

- `watchPosition` 持续上报位置变化，适合导航与运动轨迹；
- 返回的 `watchId` 用于停止监听，不再需要时必须 `clearWatch`；
- 持续定位耗电且涉及隐私，离开页面或任务完成立即停止。

## 2. Haversine 距离计算

一句话版：把两点的经纬度换算成球面距离，公式如下（进阶内容，实际项目可直接用现成库）：

$$
d = 2r \cdot \arcsin\left(\sqrt{\sin^2\left(\frac{\varphi_2 - \varphi_1}{2}\right) + \cos(\varphi_1) \cos(\varphi_2) \sin^2\left(\frac{\lambda_2 - \lambda_1}{2}\right)}\right)
$$

```javascript
function haversineDistance(lat1, lon1, lat2, lon2) {
  const R = 6371;
  const toRad = (deg) => (deg * Math.PI) / 180;
  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;
  return R * 2 * Math.asin(Math.sqrt(a));
}
```

**讲解：** 经纬度是球面坐标，不能直接当平面坐标相减。Haversine 公式计算大圆距离，`r` 是地球半径（约 6371 公里），结果单位为公里。需要精确距离时推荐使用 turf.js 等库。

## 3. 地理围栏

```javascript
class Geofence {
  constructor(centerLat, centerLng, radiusMeters) {
    this.center = { lat: centerLat, lng: centerLng };
    this.radius = radiusMeters;
  }
  contains(lat, lng) {
    return haversineDistance(this.center.lat, this.center.lng, lat, lng) * 1000 <= this.radius;
  }
}
```

**讲解：**

- 地理围栏 = “圆心（经纬度）+ 半径”，用 Haversine 距离判断点是否在范围内；
- `contains` 返回布尔值，可驱动“进入/离开区域”的业务逻辑；
- 实际项目可配合 `watchPosition` 持续判断，实现到店提醒等场景。

## 4. 进阶知识点

### 4.1 Permissions API 权限查询

```javascript
navigator.permissions.query({ name: 'geolocation' }).then((result) => {
  console.log('权限状态:', result.state); // granted | denied | prompt
  result.onchange = () => {
    console.log('权限变更:', result.state);
  };
});
```

**讲解：**

- `permissions.query` 可提前查询权限状态，避免直接调用后才发现被拒绝；
- `state` 三种取值：`granted` 已授权、`denied` 已拒绝、`prompt` 等待询问；
- `onchange` 监听权限变化（如用户在设置中改了授权）。

## 5. 动手试试

### 入门版（必做）

1. 在页面显示“获取我的位置”按钮，点击后调用 `getCurrentPosition` 展示经纬度与精度；
2. 拒绝授权一次，观察错误分支的提示；
3. 用高德或腾讯地图的 JS API，把坐标显示到地图上。

### 进阶版（选做）

1. 用 `watchPosition` 实现“移动距离统计”，累积相邻两点间的 Haversine 距离；
2. 用 Permissions API 在调用前查询权限状态并提示用户；
3. 实现一个简单的“进入店铺范围提醒”地理围栏。

## 6. 核心知识点

> 一句话记住定位：`getCurrentPosition` 取一次，`watchPosition` 持续跟；`clearWatch` 要记得，权限被拒要兜底。

- `getCurrentPosition(success, error, options)` 单次获取位置；
- `watchPosition` 持续监听，返回 `watchId`，用 `clearWatch` 停止；
- `position.coords` 提供经纬度、精度、海拔、速度等；
- 错误码：拒绝授权、位置不可用、超时；
- Haversine 公式计算球面距离，实际项目可用 turf.js；
- 定位涉及隐私：只在必要时申请，用完即停。

## 7. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 页面加载就请求定位 | 用户无感知，拒绝率高 | 由用户点击触发并说明用途 |
| 持续 `watchPosition` 不停止 | 耗电、隐私风险 | 用完 `clearWatch`，切后台暂停 |
| 把经纬度当平面坐标算距离 | 结果严重偏差 | 使用 Haversine 或地图库 |
| 忽略错误分支 | 拒绝后页面无反馈 | 提供降级文案与手动输入 |
| 明文传输位置 | 隐私泄露风险 | 使用 HTTPS |
| 未经许可保存位置 | 侵犯用户隐私 | 征得同意并允许删除 |

## 8. 扩展学习

- 地图服务：高德/腾讯/Google Maps JS API 的坐标展示与逆地理编码；
- 权限体系：`html5/008-HTML5OfflineStorageWebAPI` 中 Notification 等权限 API；
- 实时位置：`html5/024-WebSocket` 传输位置实现共享定位；
- 隐私合规：了解 GDPR/个人信息保护法对位置数据的处理要求。
