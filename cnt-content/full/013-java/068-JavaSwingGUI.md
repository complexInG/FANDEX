---
order: 200
tags:
  - java
difficulty: intermediate
title: 'Java Swing 图形界面'
module: java
category: 'Java Basics'
description: 'Swing 组件体系、事件驱动与 GUI 应用开发。'
author: fanquanpp
updated: '2026-08-01'
related:
  - java/网络编程
  - java/SpringCloud微服务开发
  - 'java/项目示例-图书管理系统'
  - java/理论知识点
prerequisites:
  - java/概述与开发环境
---

﻿# Java Switch 模式匹配 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. Swing 概述 | Swing Overview

Swing 是 Java 提供的一个 GUI (图形用户界面) 工具包，是 AWT (Abstract Window Toolkit) 的增强版本。Swing 提供了丰富的组件和功能，用于创建跨平台的桌面应用程序。

### 1.1 Swing 的特点

- **纯 Java 实现**：Swing 组件完全由 Java 实现，不依赖于底层操作系统的 GUI 组件
- **跨平台**：相同的 Swing 代码可以在不同的操作系统上运行，保持一致的外观和行为
- **轻量级组件**：Swing 组件不依赖于本地平台的 GUI 组件，而是在 Java 中模拟实现
- **丰富的组件**：提供了大量的 GUI 组件，如按钮、文本框、列表、表格等
- **可定制性**：可以通过 Look and Feel 机制更改应用程序的外观
- **事件驱动**：基于事件处理模型，响应用户的操作

### 1.2 Swing 与 AWT 的区别

| 特性                 | AWT                        | Swing            |
| -------------------- | -------------------------- | ---------------- |
| 实现方式             | 依赖本地平台 GUI 组件      | 纯 Java 实现     |
| 组件类型             | 重量级组件                 | 轻量级组件       |
| 外观一致性           | 依赖平台，不同平台外观不同 | 跨平台一致的外观 |
| 组件丰富度           | 基础组件                   | 丰富的组件库     |
| 性能                 | 通常更快                   | 可能稍慢但更灵活 |
| ## 2. Swing 基础组件 | Basic Components           |

Swing 提供了丰富的 GUI 组件，以下是一些常用的基础组件：

### 2.1 顶层容器

- **JFrame**：主窗口，包含标题栏、最小化/最大化/关闭按钮
- **JDialog**：对话框窗口，通常用于显示消息或获取用户输入
- **JApplet**：小程序容器，用于在网页中运行 Java 应用

### 2.2 中间组件

- **JPanel**：面板，用于组织和布局其他组件
- **JScrollPane**：带滚动条的面板，用于显示超出容器大小的内容
- **JSplitPane**：分割面板，用于将容器分为两个可调整大小的部分
- **JTabbedPane**：选项卡面板，用于在同一区域显示多个面板

### 2.3 基本控件

- **JButton**：按钮，用于触发操作
- **JTextField**：文本输入框，用于输入单行文本
- **JTextArea**：文本区域，用于输入多行文本
- **JLabel**：标签，用于显示文本或图像
- **JCheckBox**：复选框，用于选择多个选项
- **JRadioButton**：单选按钮，用于从多个选项中选择一个
- **JComboBox**：下拉列表，用于从预定义选项中选择
- **JList**：列表，用于显示多个选项
- **JTable**：表格，用于显示二维数据
- **JSlider**：滑块，用于在范围内选择值
- **JProgressBar**：进度条，用于显示操作进度

## 3. 布局管理器 | Layout Managers

布局管理器负责组件在容器中的排列方式，Swing 提供了多种布局管理器：

### 3.1 FlowLayout

- **特点**：组件按照从左到右、从上到下的顺序排列
- **适用场景**：简单的组件排列，如按钮组
- **示例**：

```java
 JPanel panel = new JPanel();
 panel.setLayout(new FlowLayout());
 panel.add(new JButton("Button 1"));
 panel.add(new JButton("Button 2"));
 panel.add(new JButton("Button 3"));
```

### 3.2 BorderLayout

- **特点**：将容器分为东、西、南、北、中五个区域
- **适用场景**：主窗口布局，如菜单栏在北，状态栏在南，内容在中
- **示例**：

```java
 JFrame frame = new JFrame("BorderLayout Example");
 frame.setLayout(new BorderLayout());
 frame.add(new JButton("North"), BorderLayout.NORTH);
 frame.add(new JButton("South"), BorderLayout.SOUTH);
 frame.add(new JButton("East"), BorderLayout.EAST);
 frame.add(new JButton("West"), BorderLayout.WEST);
 frame.add(new JButton("Center"), BorderLayout.CENTER);
```

### 3.3 GridLayout

- **特点**：将容器分为规则的网格，每个单元格大小相同
- **适用场景**：需要整齐排列的组件，如计算器按钮
- **示例**：

```java
 JPanel panel = new JPanel();
 panel.setLayout(new GridLayout(3, 3)); // 3行3列
 for (int i = 1; i <= 9; i++) {
  panel.add(new JButton("" + i));
 }
```

### 3.4 GridBagLayout

- **特点**：灵活的网格布局，可以指定组件的位置、大小和权重
- **适用场景**：复杂的布局需求
- **示例**：

```java
 JPanel panel = new JPanel();
 panel.setLayout(new GridBagLayout());
 GridBagConstraints gbc = new GridBagConstraints();
 // 添加第一个组件
 JButton button1 = new JButton("Button 1");
 gbc.gridx = 0;
 gbc.gridy = 0;
 gbc.gridwidth = 1;
 gbc.gridheight = 1;
 gbc.fill = GridBagConstraints.HORIZONTAL;
 panel.add(button1, gbc);
 // 添加第二个组件
 JButton button2 = new JButton("Button 2");
 gbc.gridx = 1;
 gbc.gridy = 0;
 gbc.gridwidth = 2;
 gbc.fill = GridBagConstraints.HORIZONTAL;
 panel.add(button2, gbc);
```

### 3.5 CardLayout

- **特点**：在同一区域显示多个组件，但每次只显示一个
- **适用场景**：选项卡式界面，如向导或多步骤表单
- **示例**：

```java
 JPanel panel = new JPanel();
 CardLayout cardLayout = new CardLayout();
 panel.setLayout(cardLayout);
 // 添加卡片
 panel.add(new JButton("Card 1"), "card1");
 panel.add(new JButton("Card 2"), "card2");
 panel.add(new JButton("Card 3"), "card3");
 // 显示特定卡片
 cardLayout.show(panel, "card2");
```

## 4. 事件处理 | Event Handling

Swing 使用事件处理模型来响应用户的操作，主要包括以下几个部分：

### 4.1 事件类型

- **ActionEvent**：按钮点击、菜单项选择等操作
- **MouseEvent**：鼠标点击、移动、拖动等操作
- **KeyEvent**：键盘按键操作
- **WindowEvent**：窗口打开、关闭、最小化等操作
- **FocusEvent**：组件获得或失去焦点的操作

### 4.2 事件监听器

事件监听器是实现了特定接口的对象，用于处理特定类型的事件：

- **ActionListener**：处理 ActionEvent
- **MouseListener**：处理 MouseEvent
- **KeyListener**：处理 KeyEvent
- **WindowListener**：处理 WindowEvent
- **FocusListener**：处理 FocusEvent

### 4.3 事件处理示例

```java
 import javax.swing.*;
 import java.awt.event.*;
 public class EventHandlingExample {
  public static void main(String[] args) {
  JFrame frame = new JFrame("Event Handling Example");
  frame.setSize(300, 200);
  frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  JPanel panel = new JPanel();
  JButton button = new JButton("Click Me");
  // 添加动作监听器
  button.addActionListener(new ActionListener() {
  @Override
  public void actionPerformed(ActionEvent e) {
  JOptionPane.showMessageDialog(frame, "Button clicked!");
  }
  });
  panel.add(button);
  frame.add(panel);
  frame.setVisible(true);
  }
 }
```

### 4.4 适配器类

为了简化事件监听器的实现，Swing 提供了适配器类，这些类实现了相应的监听器接口，但所有方法都是空实现：

- **MouseAdapter**：实现 MouseListener 接口
- **KeyAdapter**：实现 KeyListener 接口
- **WindowAdapter**：实现 WindowListener 接口
- **FocusAdapter**：实现 FocusListener 接口
  使用适配器类可以只重写需要的方法，而不是实现所有方法：

```java
 button.addMouseListener(new MouseAdapter() {
  @Override
  public void mouseClicked(MouseEvent e) {
  System.out.println("Mouse clicked!");
  }
 }
```

## 5. Swing 高级特性 | Advanced Features

### 5.1 对话框 | Dialogs

Swing 提供了多种对话框，用于显示消息、获取用户输入等：

- **JOptionPane**：显示消息、确认、输入等对话框
- **JFileChooser**：文件选择对话框
- **JColorChooser**：颜色选择对话框
  示例：

```java
 // 显示消息对话框
 JOptionPane.showMessageDialog(frame, "Hello, Swing!");
 // 显示确认对话框
 int option = JOptionPane.showConfirmDialog(frame, "Are you sure?");
 if (option == JOptionPane.YES_OPTION) {
  System.out.println("User clicked Yes");
 }
 // 显示输入对话框
 String input = JOptionPane.showInputDialog(frame, "Enter your name:");
 System.out.println("User entered: " + input);
 // 显示文件选择对话框
 JFileChooser fileChooser = new JFileChooser();
 int result = fileChooser.showOpenDialog(frame);
 if (result == JFileChooser.APPROVE_OPTION) {
  System.out.println("Selected file: " + fileChooser.getSelectedFile());
 }
 // 显示颜色选择对话框
 Color color = JColorChooser.showDialog(frame, "Choose a color", Color.RED);
 System.out.println("Selected color: " + color);
```

### 5.2 菜单 | Menus

Swing 提供了完整的菜单系统，包括菜单栏、菜单和菜单项：

```java
 JFrame frame = new JFrame("Menu Example");
 frame.setSize(400, 300);
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 // 创建菜单栏
 JMenuBar menuBar = new JMenuBar();
 // 创建文件菜单
 JMenu fileMenu = new JMenu("File");
 JMenuItem newItem = new JMenuItem("New");
 JMenuItem openItem = new JMenuItem("Open");
 JMenuItem saveItem = new JMenuItem("Save");
 JMenuItem exitItem = new JMenuItem("Exit");
 // 添加菜单项到文件菜单
 fileMenu.add(newItem);
 fileMenu.add(openItem);
 fileMenu.add(saveItem);
 fileMenu.addSeparator(); // 添加分隔线
 fileMenu.add(exitItem);
 // 创建编辑菜单
 JMenu editMenu = new JMenu("Edit");
 JMenuItem cutItem = new JMenuItem("Cut");
 JMenuItem copyItem = new JMenuItem("Copy");
 JMenuItem pasteItem = new JMenuItem("Paste");
 // 添加菜单项到编辑菜单
 editMenu.add(cutItem);
 editMenu.add(copyItem);
 editMenu.add(pasteItem);
 // 添加菜单到菜单栏
 menuBar.add(fileMenu);
 menuBar.add(editMenu);
 // 设置菜单栏
 frame.setJMenuBar(menuBar);
 // 添加退出菜单项的监听器
 exitItem.addActionListener(new ActionListener() {
  @Override
  public void actionPerformed(ActionEvent e) {
  System.exit(0);
  }
 }
 frame.setVisible(true);
```

### 5.3 表格 | Tables

JTable 组件用于显示和编辑二维数据：

```java
 JFrame frame = new JFrame("Table Example");
 frame.setSize(500, 300);
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 // 列名
 String[] columnNames = {"ID", "Name", "Age", "City"};
 // 数据
 Object[][] data = {
  {1, "John", 25, "New York"},
  {2, "Mary", 30, "London"},
  {3, "Bob", 35, "Paris"},
  {4, "Alice", 28, "Tokyo"}
 }
 // 创建表格
 JTable table = new JTable(data, columnNames);
 // 添加滚动条
 JScrollPane scrollPane = new JScrollPane(table);
 frame.add(scrollPane);
 frame.setVisible(true);
```

### 5.4 树 | Trees

JTree 组件用于显示层次结构数据：

```java
 JFrame frame = new JFrame("Tree Example");
 frame.setSize(400, 300);
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 // 创建根节点
 defaultMutableTreeNode root = new DefaultMutableTreeNode("Root");
 // 创建子节点
 defaultMutableTreeNode node1 = new DefaultMutableTreeNode("Node 1");
 defaultMutableTreeNode node2 = new DefaultMutableTreeNode("Node 2");
 defaultMutableTreeNode node3 = new DefaultMutableTreeNode("Node 3");
 // 添加子节点到根节点
 root.add(node1);
 root.add(node2);
 root.add(node3);
 // 创建子子节点
 defaultMutableTreeNode node1_1 = new DefaultMutableTreeNode("Node 1.1");
 defaultMutableTreeNode node1_2 = new DefaultMutableTreeNode("Node 1.2");
 node1.add(node1_1);
 node1.add(node1_2);
 // 创建树
 JTree tree = new JTree(root);
 // 添加滚动条
 JScrollPane scrollPane = new JScrollPane(tree);
 frame.add(scrollPane);
 frame.setVisible(true);
```

## 6. 外观与感觉 | Look and Feel

Swing 允许通过 Look and Feel (L&F) 机制更改应用程序的外观：

### 6.1 内置的 Look and Feel

- **Metal**：默认的跨平台外观
- **Nimbus**：现代的跨平台外观
- **Windows**：Windows 风格的外观
- **Windows Classic**：经典 Windows 风格的外观
- **Motif**：Unix/Linux 风格的外观
- **Mac OS X**：Mac 风格的外观（仅在 Mac 系统上可用）

### 6.2 设置 Look and Feel

```java
 import javax.swing.*;
 import javax.swing.plaf.nimbus.NimbusLookAndFeel;
 public class LookAndFeelExample {
  public static void main(String[] args) {
  try {
  // 设置 Nimbus Look and Feel
  UIManager.setLookAndFeel(new NimbusLookAndFeel());
  // 或者使用系统默认的 Look and Feel
  // UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
  } catch (Exception e) {
  e.printStackTrace();
  }
  // 创建并显示 GUI
  JFrame frame = new JFrame("Look and Feel Example");
  frame.setSize(300, 200);
  frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  JPanel panel = new JPanel();
  panel.add(new JButton("Button"));
  panel.add(new JTextField(20));
  panel.add(new JCheckBox("Check Box"));
  frame.add(panel);
  frame.setVisible(true);
  }
 }
```

## 7. 实战示例 | Practical Examples

### 7.1 简单的计算器

```java
 import javax.swing.*;
 import java.awt.*;
 import java.awt.event.*;
 public class Calculator {
  private JFrame frame;
  private JTextField textField;
  private String operator = "";
  private double firstNumber = 0;
  private boolean start = true;
  public Calculator() {
  frame = new JFrame("Calculator");
  frame.setSize(300, 400);
  frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  frame.setLayout(new BorderLayout());
  // 创建文本框
  textField = new JTextField();
  textField.setFont(new Font("Arial", Font.PLAIN, 24));
  textField.setHorizontalAlignment(JTextField.RIGHT);
  frame.add(textField, BorderLayout.NORTH);
  // 创建按钮面板
  JPanel buttonPanel = new JPanel();
  buttonPanel.setLayout(new GridLayout(4, 4, 5, 5));
  // 按钮标签
  String[] buttons = {
  "7", "8", "9", "/",
  "4", "5", "6", "*",
  "1", "2", "3", "-",
  "C", "0", "=", "+"
  };
  // 创建并添加按钮
  for (String button : buttons) {
  JButton btn = new JButton(button);
  btn.setFont(new Font("Arial", Font.PLAIN, 18));
  btn.addActionListener(new ButtonClickListener());
  buttonPanel.add(btn);
  }
  frame.add(buttonPanel, BorderLayout.CENTER);
  frame.setVisible(true);
  }
  private class ButtonClickListener implements ActionListener {
  @Override
  public void actionPerformed(ActionEvent e) {
  String command = e.getActionCommand();
  if (command.charAt(0) >= '0' && command.charAt(0) <= '9' || command.equals(".")) {
  if (start) {
  textField.setText("");
  start = false;
  }
  textField.setText(textField.getText() + command);
  } else if (command.equals("C")) {
  textField.setText("");
  operator = "";
  firstNumber = 0;
  start = true;
  } else if (command.equals("=")) {
  double secondNumber = Double.parseDouble(textField.getText());
  double result = 0;
  switch (operator) {
  case "+":
  result = firstNumber + secondNumber;
  break;
  case "-":
  result = firstNumber - secondNumber;
  break;
  case "*":
  result = firstNumber * secondNumber;
  break;
  case "/":
  result = firstNumber / secondNumber;
  break;
  }
  textField.setText(String.valueOf(result));
  operator = "";
  start = true;
  } else {
  if (!start) {
  firstNumber = Double.parseDouble(textField.getText());
  operator = command;
  start = true;
  }
  }
  }
  }
  public static void main(String[] args) {
  new Calculator();
  }
 }
```

### 7.2 简单的文本编辑器

```java
 import javax.swing.*;
 import java.awt.*;
 import java.awt.event.*;
 import java.io.*;
 public class TextEditor {
  private JFrame frame;
  private JTextArea textArea;
  private JMenuBar menuBar;
  private JMenu fileMenu;
  private JMenuItem newItem, openItem, saveItem, exitItem;
  private File currentFile = null;
  public TextEditor() {
  frame = new JFrame("Text Editor");
  frame.setSize(600, 400);
  frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  // 创建文本区域
  textArea = new JTextArea();
  textArea.setFont(new Font("Arial", Font.PLAIN, 14));
  JScrollPane scrollPane = new JScrollPane(textArea);
  frame.add(scrollPane, BorderLayout.CENTER);
  // 创建菜单栏
  menuBar = new JMenuBar();
  // 创建文件菜单
  fileMenu = new JMenu("File");
  // 创建菜单项
  newItem = new JMenuItem("New");
  openItem = new JMenuItem("Open");
  saveItem = new JMenuItem("Save");
  exitItem = new JMenuItem("Exit");
  // 添加菜单项到文件菜单
  fileMenu.add(newItem);
  fileMenu.add(openItem);
  fileMenu.add(saveItem);
  fileMenu.addSeparator();
  fileMenu.add(exitItem);
  // 添加文件菜单到菜单栏
  menuBar.add(fileMenu);
  // 设置菜单栏
  frame.setJMenuBar(menuBar);
  // 添加事件监听器
  newItem.addActionListener(new ActionListener() {
  @Override
  public void actionPerformed(ActionEvent e) {
  textArea.setText("");
  currentFile = null;
  frame.setTitle("Text Editor");
  }
  });
  openItem.addActionListener(new ActionListener() {
  @Override
  public void actionPerformed(ActionEvent e) {
  JFileChooser fileChooser = new JFileChooser();
  int result = fileChooser.showOpenDialog(frame);
  if (result == JFileChooser.APPROVE_OPTION) {
  currentFile = fileChooser.getSelectedFile();
  try {
  BufferedReader reader = new BufferedReader(new FileReader(currentFile));
  textArea.read(reader, null);
  reader.close();
  frame.setTitle("Text Editor - " + currentFile.getName());
  } catch (IOException ex) {
  ex.printStackTrace();
  }
  }
  }
  });
  saveItem.addActionListener(new ActionListener() {
  @Override
  public void actionPerformed(ActionEvent e) {
  if (currentFile == null) {
  JFileChooser fileChooser = new JFileChooser();
  int result = fileChooser.showSaveDialog(frame);
  if (result == JFileChooser.APPROVE_OPTION) {
  currentFile = fileChooser.getSelectedFile();
  } else {
  return;
  }
  }
  try {
  BufferedWriter writer = new BufferedWriter(new FileWriter(currentFile));
  textArea.write(writer);
  writer.close();
  frame.setTitle("Text Editor - " + currentFile.getName());
  } catch (IOException ex) {
  ex.printStackTrace();
  }
  }
  });
  exitItem.addActionListener(new ActionListener() {
  @Override
  public void actionPerformed(ActionEvent e) {
  System.exit(0);
  }
  });
  frame.setVisible(true);
  }
  public static void main(String[] args) {
  new TextEditor();
  }
 }
```

## 8. 最佳实践 | Best Practices

### 8.1 性能优化

- **使用合适的布局管理器**：根据界面需求选择合适的布局管理器
- **避免过度使用重量级组件**：重量级组件可能影响性能
- **使用 SwingUtilities.invokeLater**：确保 GUI 操作在事件分发线程中执行
- **合理使用组件**：只创建必要的组件，避免创建过多组件

### 8.2 代码组织

- **使用 MVC 模式**：将模型、视图和控制器分离
- **模块化设计**：将功能划分为模块，提高代码可维护性
- **命名规范**：使用清晰的命名规范，提高代码可读性
- **注释**：添加适当的注释，说明代码的功能和逻辑

### 8.3 用户体验

- **响应式设计**：确保界面在不同大小的窗口中都能正常显示
- **合理的布局**：使用合理的布局，使界面美观易用
- **适当的反馈**：对用户操作提供适当的反馈，如进度条、消息框等
- **快捷键**：为常用操作提供快捷键，提高用户操作效率

## 9. 总结 | Summary

Swing 是 Java 提供的功能强大的 GUI 工具包，通过它可以创建跨平台的桌面应用程序。Swing 提供了丰富的组件和功能，包括各种控件、布局管理器、事件处理机制等。
通过学习 Swing，你可以创建各种类型的桌面应用程序，从简单的计算器到复杂的文本编辑器。在实际开发中，应根据具体需求选择合适的组件和布局管理器，并遵循相关的最佳实践，以创建美观、高效、用户友好的应用程序。
## 类型模式

**基本写法：instanceof 类型模式**
`if (<变量> instanceof <类型> <变量名>) { ... }`
```java
// Java 16+，类型转换自动绑定变量
Object obj = "hello";
if (obj instanceof String s) {
    System.out.println(s.length());
}
```

---

**基本写法：switch 类型模式**
`case <类型> <变量名> -> <结果>;`
```java
// Java 21 正式，按类型分支
static String format(Object obj) {
    return switch (obj) {
        case Integer i -> "int: " + i;
        case String s  -> "str: " + s;
        case null      -> "null";
        default        -> "other";
    };
}
```

---

## 守卫模式

**基本写法：when 条件守卫**
`case <类型> <变量名> when <条件> -> <结果>;`
```java
// Java 21 正式，在 case 后追加条件
static String classify(Integer i) {
    return switch (i) {
        case Integer v when v > 0  -> "positive";
        case Integer v when v == 0 -> "zero";
        case Integer v             -> "negative";
    };
}
```

---

## null 处理

**基本写法：显式 null 分支**
`case null -> <结果>;`
```java
// Java 21，switch 内直接处理 null
String label = switch (obj) {
    case null      -> "N/A";
    case String s  -> s;
    default        -> obj.toString();
};
```

---

**基本写法：null 合并分支**
`case null, default -> <结果>;`
```java
// null 与 default 合并处理
String label = switch (obj) {
    case String s -> s;
    case null, default -> "fallback";
};
```

---

## 记录模式

**基本写法：解构记录**
`case <记录名>(<组件1>, <组件2>) -> <结果>;`
```java
// Java 21 正式，解构 record 组件
record Point(int x, int y) {}
static int sum(Point p) {
    return switch (p) {
        case Point(int x, int y) -> x + y;
    };
}
```

---

**基本写法：嵌套记录模式**
`case <外层>(<内层>, <值>) -> <结果>;`
```java
// 嵌套解构
record Point(int x, int y) {}
record Line(Point start, Point end) {}
static String desc(Line l) {
    return switch (l) {
        case Line(Point(int x1, int y1), Point(int x2, int y2))
            -> "(" + x1 + "," + y1 + ")->(" + x2 + "," + y2 + ")";
    };
}
```

---

**基本写法：类型 + 守卫结合**
`case <类型> <名> when <条件> -> <结果>;`
```java
// 组合类型模式与守卫
record Point(int x, int y) {}
static String where(Point p) {
    return switch (p) {
        case Point(int x, int y) when x == y -> "diagonal";
        case Point(int x, int y)             -> "other";
    };
}
```

---

## 穷举性与密封类

**基本写法：密封类穷举**
`sealed interface <名称> permits <子类1>, <子类2>`
```java
// 密封层级 + switch 穷举，无需 default
sealed interface Shape permits Circle, Square {}
record Circle(double r) implements Shape {}
record Square(double s) implements Shape {}

static double area(Shape s) {
    return switch (s) {
        case Circle c -> Math.PI * c.r() * c.r();
        case Square q -> q.s() * q.s();
    };
}
```

---

**基本写法：未命名模式变量**
`case <类型> _ -> <结果>;`
```java
// Java 22+，不需要组件值时用 _ 占位
static boolean isCircle(Shape s) {
    return switch (s) {
        case Circle _ -> true;
        case Square _ -> false;
    };
}
```

---

## 表达式与语句

**基本写法：switch 表达式**
`switch (<值>) { case ... -> <结果>; }`
```java
// 返回值，用 -> 箭头
int len = switch (s) {
    case null -> 0;
    case String v -> v.length();
};
```

---

**基本写法：switch 语句带 yield**
`switch (<值>) { case <模式>: yield <值>; }`
```java
// 块语句中用 yield 返回
int len = switch (s) {
    case String v: {
        System.out.println("got string");
        yield v.length();
    }
    case null: yield 0;
};
```

---

## 进阶用法

**基本写法：父类型分支需在前**
`case <子类型> -> ...; case <父类型> -> ...;`
```java
// 子类型分支必须在父类型之前
static String of(Number n) {
    return switch (n) {
        case Integer i -> "int " + i;
        case Double d  -> "dbl " + d;
        case Number x  -> "num " + x;
    };
}
```

---

**基本写法：数组与集合判断**
`case <类型>[] <名> -> ...;`
```java
// 数组类型模式
static String desc(Object o) {
    return switch (o) {
        case int[] arr   -> "int[" + arr.length + "]";
        case String[] arr-> "str[" + arr.length + "]";
        default          -> "other";
    };
}
```

## 参考文献



Oracle Java 官方文档：https://docs.oracle.com/en/java/
OpenJDK 项目：https://openjdk.org/
Java 语言规范：https://docs.oracle.com/javase/specs/
Spring 官方文档：https://spring.io/projects/spring-boot
Baeldung 教程站：https://www.baeldung.com/
Maven 官方文档：https://maven.apache.org/guides/

## 延伸阅读



Java 并发与 JUC，见 013-java 模块并发文档。
JVM 内存与 GC 调优，见 013-java 模块 JVM 文档。
Spring Boot 微服务与 Kubernetes，见 013-java/041-JavaKubernetes 文档。
数据库访问（JDBC/JPA），见 019-sql 模块相关文档。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Java 全栈课程；尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Java 进阶课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Java 概述与开发环境 | 001-JavaOverviewDevEnv | 本文的前置基础 |
| 快速入门 | 002-QuickStart | 本文的前置基础 |
| 程序结构与基本语法 | 003-ProgramStructureBasicSyntax | 本文的并列主题 |
| 数据类型与类型转换 | 004-DataTypeConversion | 本文的并列主题 |
| 变量与常量 | 005-VariableConstant | 本文的并列主题 |
| 枚举与注解 | 006-JavaAnnotationsTutorial | 本文的并列主题 |
| 泛型进阶 | 007-JavaGenericsTutorial | 本文的并列主题 |
| 并发编程基础 | 008-ConcurrencyBasics | 本文的前置基础 |
| JUC并发包 | 009-JUCConcurrency | 本文的并列主题 |
| JVM类加载机制 | 010-JVMClassLoadingMechanism | 本文的原理深化 |
| JVM垃圾回收 | 011-JVMGC | 本文的并列主题 |
| Java反射 | 012-JavaReflection | 本文的并列主题 |
| Java序列化 | 013-JavaSerialization | 本文的并列主题 |
| JavaIO与NIO | 014-JavaIONIO | 本文的并列主题 |
| Java新特性 | 015-JavaNewFeatures | 本文的并列主题 |
| 运算符与表达式 | 016-OperatorExpression | 本文的并列主题 |
| Spring 基础：IoC 容器、AOP、Bean 生命周期与企业级开发核心 | 017-SpringBasicsIoCAOPBeanLifecycle | 本文的前置基础 |
| SpringBoot进阶 | 018-SpringBootAdvanced | 本文的并列主题 |
| SpringBoot安全 | 019-SpringBootSecurity | 本文的安全延伸 |
| SpringBoot数据访问 | 020-SpringBootDataAccess | 本文的并列主题 |
| Java设计模式 | 021-JavaDesignPattern | 本文的并列主题 |
| Java函数式编程 | 022-JavaFunctionalProgramming | 本文的并列主题 |
| Java网络编程 | 023-JavaNetworkProgramming | 本文的并列主题 |
| Java日志系统 | 024-JavaLogSystem | 本文的并列主题 |
| Java单元测试 | 025-JavaUnitTest | 本文的并列主题 |
| Java构建工具 | 026-JavaBuildTool | 本文的并列主题 |
| 控制流 | 027-ControlFlow | 本文的并列主题 |
| Java与微服务 | 028-JavaMicroservice | 本文的并列主题 |
| Java与消息队列 | 029-JavaMessageQueue | 本文的并列主题 |
| Java与Redis | 030-JavaRedis | 本文的并列主题 |
| Java与Docker | 031-JavaDocker | 本文的并列主题 |
| Java与GraphQL | 032-JavaGraphQL | 本文的并列主题 |
| Java性能调优 | 033-JavaPerformanceTuning | 本文的性能延伸 |
| Java与AI | 034-JavaAI | 本文的并列主题 |
| Java与安全 | 035-JavaSecurity | 本文的安全延伸 |
| Java与WebAssembly | 036-JavaWebAssembly | 本文的并列主题 |
| Java与响应式编程 | 037-JavaReactiveProgramming | 本文的并列主题 |
| 方法详解 | 038-MethodDetailed | 本文的并列主题 |
| Java与虚拟线程 | 039-JavaVirtualThread | 本文的并列主题 |
| Java与GraalVM | 040-JavaGraalVM | 本文的并列主题 |
| Java与Kubernetes | 041-JavaKubernetes | 本文的并列主题 |
| Java记录类 | 042-JavaRecordClass | 本文的并列主题 |
| Java文本块 | 043-JavaTextBlock | 本文的并列主题 |
| Java模块系统 | 044-JavaModuleSystem | 本文的并列主题 |
| Java与数据库连接 | 045-JavaDatabaseConnection | 本文的并列主题 |
| Java 新特性与生态 | 046-JavaNewFeaturesEcosystem | 本文的并列主题 |
| 数组详解 | 047-ArrayDetailed | 本文的并列主题 |
| JVM调优 | 048-JVMtuning | 本文的性能延伸 |
| 集合框架详解 | 049-CollectionFrameworkDetailed | 本文的并列主题 |
| 并发编程详解 | 050-ConcurrencyDetailed | 本文的并列主题 |
| CompletableFuture异步编排 | 051-CompletableFutureAsync | 本文的并列主题 |
| ThreadLocal内存泄漏 | 052-ThreadLocalMemoryLeak | 本文的并列主题 |
| 反射与动态代理 | 053-ReflectionDynamicProxy | 本文的并列主题 |
| 注解处理器 | 054-AnnotationProcessor | 本文的并列主题 |
| 分代ZGC详解 | 055-GenerationalZGCDetailed | 本文的并列主题 |
| 面向对象编程 | 056-OOP | 本文的并列主题 |
| 抽象类与接口 | 057-AbstractClassInterface | 本文的并列主题 |
| 异常处理机制 | 058-ExceptionHandlingMechanism | 本文的原理深化 |
| 泛型详解 | 059-GenericDetailed | 本文的并列主题 |
| I/O 流与文件操作 | 060-IOStreamFileOperation | 本文的并列主题 |
| 多线程基础 | 061-MultithreadingBasics | 本文的前置基础 |
| JVM 内存模型 | 062-JVMMemoryModel | 本文的并列主题 |
| Lambda与函数式编程 | 063-LambdaFunctionalProgramming | 本文的并列主题 |
| Stream API | 064-StreamAPI | 本文的并列主题 |
| Spring Boot 学习笔记 | 065-SpringBootNotes | 本文的并列主题 |
| 网络编程 | 066-NetworkProgramming | 本文的并列主题 |
| Spring Cloud 微服务开发 | 067-SpringCloudMicroserviceDevelopment | 本文的并列主题 |
| Java Swing 图形界面 | 068-JavaSwingGUI | 本文自身 |
| Java 项目示例：图书管理系统 | 069-JavaProjectExampleLibrarySystem | 本文的综合应用 |
| Java 理论知识点：JVM 原理、类加载机制与内存管理 | 070-JavaTheoryJVMClassLoadingMemory | 本文的原理深化 |
| Java NIO 通道与缓冲区 | 071-JavaNIOChannelBuffer | 本文的并列主题 |
| Java JDBC 数据库连接 | 072-JDBCDatabaseConnection | 本文的并列主题 |
| Java Optional 类 | 073-JavaOptionalClass | 本文的并列主题 |
| Java Executor 与 ForkJoin | 074-ExecutorForkJoinPool | 本文的并列主题 |
| Java Path 与 Files 语法速查手册 | 075-JavaPathFiles | 本文的并列主题 |
| 启动 REPL 交互环境 | 076-JavaJshellJpackage | 本文的前置基础 |
| Java 同步器 CountDownLatch/CyclicBarrier/Phaser 语法速查手册 | 077-JavaCountDownLatchCyclicBarrier | 本文的并列主题 |
| Java 阻塞队列 BlockingQueue 语法速查手册 | 078-JavaBlockingQueue | 本文的并列主题 |
| Java try-with-resources 与异常链语法速查手册 | 079-JavaTryWithResources | 本文的并列主题 |
| Java HttpClient 与 WebSocket 语法速查手册 | 080-JavaHttpClientWebSocket | 本文的并列主题 |
| Java 时间格式化 DateTimeFormatter/ZoneId 语法速查手册 | 081-JavaTimeFormatting | 本文的并列主题 |
| Java 类型擦除与桥接方法语法速查手册 | 082-JavaTypeErasure | 本文的并列主题 |
| Java 枚举进阶 EnumSet/EnumMap/枚举单例语法速查手册 | 083-JavaEnumAdvanced | 本文的并列主题 |
| Java Iterator/Iterable/Spliterator 语法速查手册 | 084-JavaIteratorIterable | 本文的并列主题 |
| Java Comparator/Comparable 语法速查手册 | 085-JavaComparatorComparable | 本文的并列主题 |
| Java String.format/printf/MessageFormat 语法速查手册 | 086-JavaStringFormat | 本文的并列主题 |
| Java Arrays 工具类语法速查手册 | 087-JavaArraysUtility | 本文的并列主题 |
| Java Objects 工具类语法速查手册 | 088-JavaObjectsUtility | 本文的并列主题 |
| Java 命令行工具 javac/java/jar/jshell/jpackage 语法速查手册 | 089-JavaCommandLineTools | 本文的并列主题 |
| Maven pom.xml 配置语法速查手册 | 090-MavenPomConfiguration | 本文的并列主题 |
| Gradle build.gradle 配置语法速查手册 | 091-GradleBuildConfiguration | 本文的并列主题 |
