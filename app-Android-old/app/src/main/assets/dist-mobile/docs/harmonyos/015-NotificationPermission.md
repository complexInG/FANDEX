### 进度通知

```typescript
import notificationManager from '@ohos.notificationManager'

@Component
struct ProgressNotificationDemo {
  @State progress: number = 0
  private timer: number = -1

  // 发送带进度的通知
  sendProgressNotification(currentProgress: number) {
    const isOngoing = currentProgress < 100

    const request: notificationManager.NotificationRequest = {
      id: 100,
      isOngoing: isOngoing, // 进行中通知，不可滑动删除
      isUnremovable: isOngoing,
      content: {
        contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
          title: '文件下载',
          text: isOngoing ? `正在下载 ${currentProgress}%` : '下载完成',
        },
      },
    }

    // 设置进度条
    if (isOngoing) {
      request.template = {
        name: 'downloadTemplate',
        data: {
          progressValue: currentProgress.toString(),
          progressMaxValue: '100',
        },
      }
    }

    notificationManager.publish(request)
  }

  // 模拟下载进度
  startDownload() {
    this.progress = 0
    this.timer = setInterval(() => {
      this.progress += 5
      this.sendProgressNotification(this.progress)

      if (this.progress >= 100) {
        clearInterval(this.timer)
      }
    }, 500)
  }

  build() {
    Column({ space: 10 }) {
      Text(`下载进度: ${this.progress}%`)
      Button('开始下载')
        .onClick(() => this.startDownload())
    }
    .padding(20)
  }
}
```

### 通知点击跳转

```typescript
import notificationManager from '@ohos.notificationManager';
import wantAgent from '@ohos.app.ability.wantAgent';

async function sendClickableNotification(context: Context) {
  // 创建点击通知后的意图
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: context.abilityInfo.bundleName,
        abilityName: 'DetailAbility',
        parameters: {
          id: '123',
        },
      },
    ],
    operationType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG],
  };

  const pendingWantAgent = await wantAgent.getWantAgent(wantAgentInfo);

  // 发送带点击意图的通知
  const request: notificationManager.NotificationRequest = {
    id: 200,
    wantAgent: pendingWantAgent,
    content: {
      contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal: {
        title: '订单通知',
        text: '您的订单已发货，点击查看详情',
      },
    },
  };

  notificationManager.publish(request);
}
```

### 通知组管理

```typescript
import notificationManager from '@ohos.notificationManager';

// 设置通知组
function sendGroupedNotification() {
  // 社交消息组
  const socialRequest: notificationManager.NotificationRequest = {
    id: 301,
    groupName: 'social_messages',
    content: {
      contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal: {
        title: '张三',
        text: '周末有空吗？',
      },
    },
  };

  // 系统消息组
  const systemRequest: notificationManager.NotificationRequest = {
    id: 302,
    groupName: 'system_alerts',
    content: {
      contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal: {
        title: '系统更新',
        text: '新版本可用',
      },
    },
  };

  notificationManager.publish(socialRequest);
  notificationManager.publish(systemRequest);
}

// 取消指定组的通知
async function cancelGroupNotifications(groupName: string) {
  await notificationManager.removeGroupByBundle(groupName);
}
```

## 概述

HarmonyOS 的通知系统允许应用向用户发送提醒信息，包括基本文本通知、进度通知和自定义通知等。权限管理系统则控制应用对系统资源和用户隐私数据的访问，分为系统授权和用户授权两种类型。合理使用通知和权限是构建安全、用户友好的应用的关键。通知需要遵循平台规范，避免频繁打扰用户；权限应按需申请，并在不需要时及时释放。

## 基础概念

**通知类型**：HarmonyOS 支持多种通知类型，包括基本文本通知（NOTIFICATION_CONTENT_BASIC_TEXT）、长文本通知（NOTIFICATION_CONTENT_LONG_TEXT）、多行文本通知（NOTIFICATION_CONTENT_MULTILINE）和图片通知（NOTIFICATION_CONTENT_PICTURE）。

**通知槽（Slot）**：通知渠道，用于对通知进行分类管理。每个通知槽可以设置不同的声音、振动和重要级别。类似 Android 的 NotificationChannel。

**系统授权权限**：在 module.json5 中声明即可自动授予的权限，如网络访问权限。这类权限不涉及用户隐私。

**用户授权权限**：需要用户在运行时明确授权的权限，如相机、麦克风、位置等。应用需要在 module.json5 中声明，并通过 API 请求用户授权。

**权限等级**：权限分为 normal（普通）、system_basic（系统基础）和 system_core（系统核心）三个等级。普通应用只能申请 normal 级别的权限。

## 快速上手

### 发送基本通知

```typescript
import notificationManager from '@ohos.notificationManager';

// 发送简单文本通知
function sendBasicNotification() {
  const request: notificationManager.NotificationRequest = {
    id: 1,
    content: {
      contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal: {
        title: '消息提醒',
        text: '您有一条新消息',
      },
    },
  };

  notificationManager
    .publish(request)
    .then(() => {
      console.info('通知发送成功');
    })
    .catch((error: Error) => {
      console.error(`通知发送失败: ${error.message}`);
    });
}
```

### 请求用户权限

```typescript
import abilityAccessCtrl from '@ohos.abilityAccessCtrl';

async function requestCameraPermission(context: Context): Promise<boolean> {
  const atManager = abilityAccessCtrl.createAtManager();

  try {
    // 先检查是否已授权
    const grantStatus = await atManager.checkAccessToken(
      getContext(context).applicationInfo.accessTokenId,
      'ohos.permission.CAMERA'
    );

    if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
      return true;
    }

    // 请求授权
    const result = await atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']);

    // 检查用户是否授权
    return result.authResults[0] === 0;
  } catch (error) {
    console.error(`权限请求失败: ${error}`);
    return false;
  }
}
```

### 声明权限

```typescript
// 在 module.json5 中声明所需权限
// {
//   "module": {
//     "requestPermissions": [
//       {
//         "name": "ohos.permission.INTERNET",
//         "reason": "$string:internet_reason",
//         "usedScene": {
//           "abilities": ["EntryAbility"],
//           "when": "inuse"
//         }
//       },
//       {
//         "name": "ohos.permission.CAMERA",
//         "reason": "$string:camera_reason",
//         "usedScene": {
//           "abilities": ["EntryAbility"],
//           "when": "inuse"
//         }
//       }
//     ]
//   }
// }
```

## 详细用法

### 多种通知类型

```typescript
import notificationManager from '@ohos.notificationManager';

// 长文本通知
function sendLongTextNotification() {
  const request: notificationManager.NotificationRequest = {
    id: 2,
    content: {
      contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_LONG_TEXT,
      longText: {
        title: '系统更新',
        text: '点击查看详情',
        longText:
          '本次更新包含多项性能优化和安全修复，建议所有用户尽快升级。主要更新内容包括：修复了蓝牙连接稳定性问题、优化了电池续航表现、增强了系统安全防护能力。',
        briefText: '系统更新可用',
      },
    },
  };

  notificationManager.publish(request);
}

// 多行文本通知
function sendMultiLineNotification() {
  const request: notificationManager.NotificationRequest = {
    id: 3,
    content: {
      contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_MULTILINE,
      multiLine: {
        title: '待办事项',
        text: '今日待办',
        briefText: '3项待办',
        lines: ['上午10:00 项目会议', '下午2:00 代码评审', '下午5:00 提交周报'],
      },
    },
  };

  notificationManager.publish(request);
}
```

### 通知槽管理

```typescript
import notificationManager from '@ohos.notificationManager';

// 创建通知槽
async function createNotificationSlot() {
  // 消息通知槽
  const messageSlot: notificationManager.NotificationSlot = {
    type: notificationManager.SlotType.SOCIAL_COMMUNICATION,
    level: notificationManager.SlotLevel.LEVEL_HIGH, // 高重要级别
    desc: '社交消息通知',
    sound: '', // 使用默认声音
    vibrationValues: [100, 200, 100, 200], // 振动模式
  };

  // 服务通知槽
  const serviceSlot: notificationManager.NotificationSlot = {
    type: notificationManager.SlotType.SERVICE_INFORMATION,
    level: notificationManager.SlotLevel.LEVEL_DEFAULT,
    desc: '服务提醒通知',
  };

  // 添加通知槽
  await notificationManager.addSlot(messageSlot);
  await notificationManager.addSlot(serviceSlot);
}

// 使用指定通知槽发送通知
function sendSlotNotification() {
  const request: notificationManager.NotificationRequest = {
    id: 10,
    slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
    content: {
      contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal: {
        title: '新消息',
        text: '张三: 你好！',
      },
    },
  };

  notificationManager.publish(request);
}
```

### 多权限批量请求

```typescript
import abilityAccessCtrl from '@ohos.abilityAccessCtrl';

async function requestMultiplePermissions(context: Context) {
  const atManager = abilityAccessCtrl.createAtManager();

  // 需要请求的权限列表
  const permissions: string[] = [
    'ohos.permission.CAMERA',
    'ohos.permission.MICROPHONE',
    'ohos.permission.LOCATION',
    'ohos.permission.APPROXIMATELY_LOCATION',
  ];

  try {
    // 批量请求权限
    const result = await atManager.requestPermissionsFromUser(context, permissions);

    // 检查每个权限的授权结果
    const granted: string[] = [];
    const denied: string[] = [];

    permissions.forEach((permission, index) => {
      if (result.authResults[index] === 0) {
        granted.push(permission);
      } else {
        denied.push(permission);
      }
    });

    console.info(`已授权: ${granted.join(', ')}`);
    console.info(`被拒绝: ${denied.join(', ')}`);

    return { granted, denied };
  } catch (error) {
    console.error(`权限请求失败: ${error}`);
    return { granted: [], denied: permissions };
  }
}
```

## 常见场景

### 应用启动时检查权限

```typescript
import abilityAccessCtrl from '@ohos.abilityAccessCtrl'

@Entry
@Component
struct PermissionCheckPage {
  @State hasCameraPermission: boolean = false
  @State hasLocationPermission: boolean = false

  async aboutToAppear() {
    await this.checkAllPermissions()
  }

  async checkAllPermissions() {
    const atManager = abilityAccessCtrl.createAtManager()
    const tokenId = getContext(this).applicationInfo.accessTokenId

    // 检查相机权限
    const cameraStatus = await atManager.checkAccessToken(tokenId, 'ohos.permission.CAMERA')
    this.hasCameraPermission = cameraStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED

    // 检查位置权限
    const locationStatus = await atManager.checkAccessToken(tokenId, 'ohos.permission.LOCATION')
    this.hasLocationPermission = locationStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED
  }

  build() {
    Column({ space: 10 }) {
      Text('权限状态').fontSize(20).fontWeight(FontWeight.Bold)

      Row() {
        Text('相机权限')
        Text(this.hasCameraPermission ? '已授权' : '未授权')
          .fontColor(this.hasCameraPermission ? '#4CAF50' : '#F44336')
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceBetween)

      Row() {
        Text('位置权限')
        Text(this.hasLocationPermission ? '已授权' : '未授权')
          .fontColor(this.hasLocationPermission ? '#4CAF50' : '#F44336')
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceBetween)

      Button('请求权限')
        .onClick(async () => {
          await requestMultiplePermissions(getContext(this))
          await this.checkAllPermissions()
        })
    }
    .padding(20)
  }
}
```

## 注意事项

- **通知频率**：避免在短时间内发送大量通知，系统可能会限制通知频率。建议合并同类通知，使用通知组管理。
- **权限说明**：申请用户授权权限时，必须在 module.json5 中提供 reason 字段说明使用原因，且原因描述应清晰准确，告知用户为何需要该权限。
- **权限使用场景**：声明权限时需指定 usedScene，说明权限在哪些 Ability 中使用以及是前台使用（inuse）还是后台使用（inuse/background）。
- **通知取消**：应用应提供取消通知的能力，使用 notificationManager.cancel 取消指定 ID 的通知，或使用 cancelAll 取消所有通知。
- **权限不可滥用**：只申请应用核心功能所需的权限，不要提前申请未来功能需要的权限。被用户拒绝后不要反复弹窗请求，应引导用户到设置页面手动开启。
- **后台通知限制**：后台应用发送通知受到限制，需要申请通知权限或使用后台任务。

## 进阶用法

### 权限动态检查与引导

```typescript
import abilityAccessCtrl from '@ohos.abilityAccessCtrl'

@Component
struct SmartPermissionDemo {
  @State permissionStatus: Map<string, string> = new Map()

  // 检查并请求权限，被拒绝时引导用户
  async ensurePermission(context: Context, permission: string): Promise<boolean> {
    const atManager = abilityAccessCtrl.createAtManager()
    const tokenId = context.applicationInfo.accessTokenId

    // 第一步：检查是否已授权
    const status = await atManager.checkAccessToken(tokenId, permission)
    if (status === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
      return true
    }

    // 第二步：请求权限
    const result = await atManager.requestPermissionsFromUser(context, [permission])
    if (result.authResults[0] === 0) {
      return true
    }

    // 第三步：检查是否选择了"不再询问"
    if (result.authResults[0] === -1) {
      // 用户选择了不再询问，引导到设置页面
      this.showPermissionSettingsDialog(context, permission)
    }

    return false
  }

  // 显示引导对话框
  showPermissionSettingsDialog(context: Context, permission: string) {
    // 弹出对话框引导用户前往设置页面
    AlertDialog.show({
      title: '需要权限',
      message: `应用需要${permission}权限才能正常使用此功能，请在设置中手动开启。`,
      primaryButton: {
        value: '去设置',
        action: () => {
          // 跳转到应用设置页面
          // 使用 UIAbilityContext 打开系统设置
        }
      },
      secondaryButton: {
        value: '取消',
        action: () => {}
      }
    })
  }

  build() {
    Column({ space: 10 }) {
      Button('使用相机功能')
        .onClick(async () => {
          const granted = await this.ensurePermission(getContext(this), 'ohos.permission.CAMERA')
          if (granted) {
            // 执行相机相关操作
          }
        })

      Button('使用位置功能')
        .onClick(async () => {
          const granted = await this.ensurePermission(getContext(this), 'ohos.permission.LOCATION')
          if (granted) {
            // 执行位置相关操作
          }
        })
    }
    .padding(20)
  }
}
```

### 定时通知

```typescript
import notificationManager from '@ohos.notificationManager';
import reminderAgentManager from '@ohos.reminderAgentManager';

// 发布定时提醒
async function scheduleReminder() {
  const reminderRequest: reminderAgentManager.ReminderRequestAlarm = {
    reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_ALARM,
    hour: 9, // 小时
    minute: 0, // 分钟
    daysOfWeek: [1, 2, 3, 4, 5], // 周一到周五
    title: '工作提醒',
    content: '该开始工作了',
    expiredContent: '提醒已过期',
    snoozeContent: '稍后提醒',
    actionButton: [
      {
        title: '知道了',
        type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CUSTOM,
      },
    ],
  };

  const reminderId = await reminderAgentManager.publishReminder(reminderRequest);
  console.info(`定时提醒已发布，ID: ${reminderId}`);
}

// 取消定时提醒
async function cancelReminder(reminderId: number) {
  await reminderAgentManager.cancelReminder(reminderId);
  console.info(`定时提醒已取消，ID: ${reminderId}`);
}

// 获取所有已发布的提醒
async function getAllReminders() {
  const reminders = await reminderAgentManager.getValidReminders();
  console.info(`当前有效提醒数量: ${reminders.length}`);
}
```
## 通知管理 API

**导入通知模块**
`import notificationManager from '@ohos.notificationManager';`
```typescript
import notificationManager from '@ohos.notificationManager';
```

**发布基本文本通知**
`notificationManager.publish(<request: NotificationRequest>): Promise<void>`
```typescript
const request: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: '消息提醒',
      text: '您有一条新消息',
    },
  },
};

notificationManager
  .publish(request)
  .then(() => {
    console.info('通知发送成功');
  })
  .catch((error: Error) => {
    console.error(`通知发送失败: ${error.message}`);
  });
```

**发布长文本通知**
`notificationManager.publish(<request: NotificationRequest>): Promise<void>`
```typescript
const request: notificationManager.NotificationRequest = {
  id: 2,
  content: {
    contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_LONG_TEXT,
    longText: {
      title: '系统更新',
      text: '点击查看详情',
      longText: '本次更新包含多项性能优化和安全修复,建议所有用户尽快升级。',
      briefText: '系统更新可用',
    },
  },
};

notificationManager.publish(request);
```

**发布多行文本通知**
`notificationManager.publish(<request: NotificationRequest>): Promise<void>`
```typescript
const request: notificationManager.NotificationRequest = {
  id: 3,
  content: {
    contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_MULTILINE,
    multiLine: {
      title: '待办事项',
      text: '今日待办',
      briefText: '3项待办',
      lines: ['上午10:00 项目会议', '下午2:00 代码评审', '下午5:00 提交周报'],
    },
  },
};

notificationManager.publish(request);
```

**发布图片通知**
`notificationManager.publish(<request: NotificationRequest>): Promise<void>`
```typescript
const request: notificationManager.NotificationRequest = {
  id: 4,
  content: {
    contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_PICTURE,
    picture: {
      title: '图片消息',
      text: '查看图片',
      expandedTitle: '图片详情',
      briefText: '图片通知',
      picture: {
        bundleName: 'com.example.app',
        moduleName: 'entry',
        abilityName: 'EntryAbility',
        src: '/resources/base/media/pic.png',
      },
    },
  },
};

notificationManager.publish(request);
```

**取消指定通知**
`notificationManager.cancel(<id: number>, [<label: string>]): Promise<void>`
```typescript
await notificationManager.cancel(1);
await notificationManager.cancel(2, 'label_name');
```

**取消所有通知**
`notificationManager.cancelAll(): Promise<void>`
```typescript
await notificationManager.cancelAll();
```

**获取通知槽**
`notificationManager.getSlot(<slotType: SlotType>): Promise<NotificationSlot>`
```typescript
const slot = await notificationManager.getSlot(
  notificationManager.SlotType.SOCIAL_COMMUNICATION
);
console.info(`通知槽级别: ${slot.level}`);
```

---

## ContentType 枚举

**ContentType 通知内容类型**
`notificationManager.ContentType.<TYPE>`
```typescript
notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT      // 基本文本
notificationManager.ContentType.NOTIFICATION_CONTENT_LONG_TEXT       // 长文本
notificationManager.ContentType.NOTIFICATION_CONTENT_MULTILINE       // 多行文本
notificationManager.ContentType.NOTIFICATION_CONTENT_PICTURE         // 图片
```

---

## NotificationRequest 对象

**NotificationRequest 通知请求结构**
`const request: notificationManager.NotificationRequest = { ... }`
```typescript
const request: notificationManager.NotificationRequest = {
  id: 100,                              // 通知 ID
  slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,  // 通知槽类型
  isOngoing: false,                     // 是否进行中通知(不可滑动删除)
  isUnremovable: false,                 // 是否不可移除
  smallIcon: $r('app.media.icon'),      // 小图标
  largeIcon: $r('app.media.large'),     // 大图标
  wantAgent: pendingWantAgent,          // 点击意图
  template: {                           // 通知模板
    name: 'downloadTemplate',
    data: {
      progressValue: '50',
      progressMaxValue: '100',
    },
  },
  content: {
    contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: '标题',
      text: '内容',
      additionalText: '附加文本',
    },
  },
};
```

---

## NotificationSlot 通知槽

**创建通知槽**
`notificationManager.addSlot(<slot: NotificationSlot>): Promise<void>`
```typescript
const slot: notificationManager.NotificationSlot = {
  type: notificationManager.SlotType.SOCIAL_COMMUNICATION,
  level: notificationManager.SlotLevel.LEVEL_HIGH,
  desc: '社交消息通知',
  sound: '',                              // 空字符串使用默认声音
  vibrationValues: [100, 200, 100, 200],  // 振动模式(毫秒)
  badgeFlag: true,                        // 是否显示角标
  bannerFlag: true,                       // 是否显示横幅
  lightEnabled: true,                     // 是否启用呼吸灯
  lightColor: 0xFFFF0000,                 // 呼吸灯颜色
};

await notificationManager.addSlot(slot);
```

**删除通知槽**
`notificationManager.removeSlot(<slotType: SlotType>): Promise<void>`
```typescript
await notificationManager.removeSlot(
  notificationManager.SlotType.SOCIAL_COMMUNICATION
);
```

**获取所有通知槽**
`notificationManager.getSlots(): Promise<Array<NotificationSlot>>`
```typescript
const slots = await notificationManager.getSlots();
slots.forEach((slot) => {
  console.info(`类型: ${slot.type}, 级别: ${slot.level}`);
});
```

---

## SlotType 枚举

**SlotType 通知槽类型**
`notificationManager.SlotType.<TYPE>`
```typescript
notificationManager.SlotType.UNKNOWN_TYPE             // 未知类型
notificationManager.SlotType.SOCIAL_COMMUNICATION     // 社交通信
notificationManager.SlotType.SERVICE_INFORMATION      // 服务信息
notificationManager.SlotType.CONTENT_INFORMATION      // 内容信息
notificationManager.SlotType.LIVE_VIEW                // 实时视图
notificationManager.SlotType.CUSTOMER_SERVICE         // 客服消息
notificationManager.SlotType.OTHER_TYPES              // 其他类型
```

---

## SlotLevel 枚举

**SlotLevel 通知槽级别**
`notificationManager.SlotLevel.<LEVEL>`
```typescript
notificationManager.SlotLevel.LEVEL_NONE       // 无(不显示通知)
notificationManager.SlotLevel.LEVEL_MIN        // 最低级别(无提示)
notificationManager.SlotLevel.LEVEL_LOW        // 低级别(状态栏小图标)
notificationManager.SlotLevel.LEVEL_DEFAULT    // 默认级别(状态栏 + 通知栏)
notificationManager.SlotLevel.LEVEL_HIGH       // 高级别(横幅 + 通知栏)
```

---

## 权限管理 API

**导入权限模块**
`import abilityAccessCtrl from '@ohos.abilityAccessCtrl';`
```typescript
import abilityAccessCtrl from '@ohos.abilityAccessCtrl';
```

**创建权限管理器**
`abilityAccessCtrl.createAtManager(): AtManager`
```typescript
const atManager = abilityAccessCtrl.createAtManager();
```

**检查权限授权状态**
`atManager.checkAccessToken(<tokenID: number>, <permissionName: string>): Promise<GrantStatus>`
```typescript
const atManager = abilityAccessCtrl.createAtManager();
const tokenId = getContext(this).applicationInfo.accessTokenId;

const grantStatus = await atManager.checkAccessToken(
  tokenId,
  'ohos.permission.CAMERA'
);

if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
  console.info('相机权限已授予');
} else {
  console.info('相机权限未授予');
}
```

**请求单个权限**
`atManager.requestPermissionsFromUser(<context: Context>, <permList: Array<string>>): Promise<PermissionRequestResult>`
```typescript
async function requestCameraPermission(context: Context): Promise<boolean> {
  const atManager = abilityAccessCtrl.createAtManager();

  try {
    const result = await atManager.requestPermissionsFromUser(context, [
      'ohos.permission.CAMERA',
    ]);

    if (result.authResults[0] === 0) {
      console.log('权限已授予');
      return true;
    } else {
      console.log('权限被拒绝');
      return false;
    }
  } catch (err) {
    console.error('申请权限失败:', err);
    return false;
  }
}
```

**批量请求权限**
`atManager.requestPermissionsFromUser(<context: Context>, <permList: Array<string>>): Promise<PermissionRequestResult>`
```typescript
async function requestMultiplePermissions(context: Context) {
  const atManager = abilityAccessCtrl.createAtManager();

  const permissions: string[] = [
    'ohos.permission.CAMERA',
    'ohos.permission.MICROPHONE',
    'ohos.permission.LOCATION',
    'ohos.permission.APPROXIMATELY_LOCATION',
  ];

  const result = await atManager.requestPermissionsFromUser(context, permissions);

  const granted: string[] = [];
  const denied: string[] = [];

  permissions.forEach((permission, index) => {
    if (result.authResults[index] === 0) {
      granted.push(permission);
    } else {
      denied.push(permission);
    }
  });

  console.info(`已授权: ${granted.join(', ')}`);
  console.info(`被拒绝: ${denied.join(', ')}`);

  return { granted, denied };
}
```

---

## GrantStatus 枚举

**GrantStatus 权限授权状态**
`abilityAccessCtrl.GrantStatus.<STATUS>`
```typescript
abilityAccessCtrl.GrantStatus.PERMISSION_DENIED     // 权限被拒绝 (-1)
abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED    // 权限已授予 (0)
```

---

## 权限声明配置

**module.json5 权限声明**
`"requestPermissions": [{ "name": ..., "reason": ..., "usedScene": ... }]`
```json
{
  "module": {
    "requestPermissions": [
      {
        "name": "ohos.permission.INTERNET",
        "reason": "$string:internet_reason",
        "usedScene": {
          "abilities": ["EntryAbility"],
          "when": "inuse"
        }
      },
      {
        "name": "ohos.permission.CAMERA",
        "reason": "$string:camera_reason",
        "usedScene": {
          "abilities": ["EntryAbility"],
          "when": "inuse"
        }
      },
      {
        "name": "ohos.permission.MICROPHONE",
        "reason": "$string:mic_reason",
        "usedScene": {
          "abilities": ["EntryAbility"],
          "when": "inuse"
        }
      },
      {
        "name": "ohos.permission.LOCATION",
        "reason": "$string:location_reason",
        "usedScene": {
          "abilities": ["EntryAbility"],
          "when": "inuse"
        }
      }
    ]
  }
}
```

**usedScene.when 权限使用时机**
`"when": "<inuse | always>"`
```json
{
  "usedScene": {
    "abilities": ["EntryAbility"],
    "when": "inuse"        // inuse: 前台使用 | always: 前后台使用
  }
}
```

---

## 权限等级分类

**权限等级表**
| 等级 | 示例权限 | 授权方式 |
| ---- | ---- | ---- |
| `normal` | `ohos.permission.INTERNET`、`ohos.permission.GET_NETWORK_INFO` | 安装时自动授予 |
| `system_basic` | `ohos.permission.CAMERA`、`ohos.permission.MICROPHONE`、`ohos.permission.LOCATION` | 运行时弹窗申请 |
| `system_core` | `ohos.permission.MANAGE_USERS`、`ohos.permission.REBOOT` | 仅系统应用可用 |

---

## 提醒服务 API

**导入提醒服务模块**
`import reminderAgentManager from '@ohos.reminderAgentManager';`
```typescript
import reminderAgentManager from '@ohos.reminderAgentManager';
```

**发布倒计时提醒**
`reminderAgentManager.publishReminder(<reminder: ReminderRequest>): Promise<number>`
```typescript
const reminderRequest: reminderAgentManager.ReminderRequestTimer = {
  reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 3600,     // 1 小时后触发
  actionButton: [
    {
      title: '关闭',
      type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE,
    },
    {
      title: '自定义',
      type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CUSTOM,
    },
  ],
  wantAgent: {
    pkgName: 'com.example.app',
    abilityName: 'EntryAbility',
  },
  maxScreenWantAgent: {
    pkgName: 'com.example.app',
    abilityName: 'EntryAbility',
  },
  notificationId: 100,
  title: '提醒标题',
  content: '提醒内容',
};

const reminderId = await reminderAgentManager.publishReminder(reminderRequest);
console.info(`提醒已发布, ID: ${reminderId}`);
```

**发布日历提醒**
`reminderAgentManager.publishReminder(<reminder: ReminderRequestCalendar>): Promise<number>`
```typescript
const calendarReminder: reminderAgentManager.ReminderRequestCalendar = {
  reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_CALENDAR,
  dateTime: {
    year: 2026,
    month: 12,
    day: 31,
    hour: 23,
    minute: 59,
  },
  daysOfWeek: [1, 2, 3, 4, 5],   // 周一到周五重复
  title: '下班提醒',
  content: '该下班啦',
  notificationId: 101,
};

const reminderId = await reminderAgentManager.publishReminder(calendarReminder);
```

**取消提醒**
`reminderAgentManager.cancelReminder(<reminderId: number>): Promise<void>`
```typescript
await reminderAgentManager.cancelReminder(reminderId);
```

**取消所有提醒**
`reminderAgentManager.cancelAllReminders(): Promise<void>`
```typescript
await reminderAgentManager.cancelAllReminders();
```

**获取有效提醒**
`reminderAgentManager.getValidReminders(): Promise<Array<ReminderRequest>>`
```typescript
const reminders = await reminderAgentManager.getValidReminders();
reminders.forEach((reminder) => {
  console.info(`提醒 ID: ${reminder.notificationId}`);
});
```

---

## ReminderType 枚举

**ReminderType 提醒类型**
`reminderAgentManager.ReminderType.<TYPE>`
```typescript
reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER      // 倒计时提醒
reminderAgentManager.ReminderType.REMINDER_TYPE_CALENDAR   // 日历提醒
reminderAgentManager.ReminderType.REMINDER_TYPE_ALARM      // 闹钟提醒
```

**ActionButtonType 按钮类型**
`reminderAgentManager.ActionButtonType.<TYPE>`
```typescript
reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE     // 关闭按钮
reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CUSTOM     // 自定义按钮
reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE     // 稍后提醒按钮
```
