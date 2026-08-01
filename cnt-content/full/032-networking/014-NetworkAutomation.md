---
order: 60
title: 网络自动化
module: networking
category: 网络技术
difficulty: advanced
description: 网络自动化：基础设施即代码、NetDevOps、网络CI/CD与自动化运维
author: fanquanpp
updated: '2026-08-01'
related:
  - networking/DNS与DHCP
  - networking/负载均衡技术
  - networking/负载均衡算法
  - networking/高可用LVS
prerequisites:
  - networking/网络基础与协议
---

## 1. NetDevOps 概述

### 1.1 核心理念

将 DevOps 实践应用于网络：

- 版本控制网络配置
- 自动化测试和部署
- 持续集成/持续交付
- 基础设施即代码

### 1.2 工具链

| 类别     | 工具                |
| -------- | ------------------- |
| 配置管理 | Ansible, Salt       |
| 模板引擎 | Jinja2              |
| 版本控制 | Git                 |
| CI/CD    | GitLab CI, Jenkins  |
| 验证     | Batfish, pyATS      |
| 监控     | Prometheus, Grafana |

## 2. 网络配置即代码

### 2.1 Git 工作流

```
main分支（生产配置）
  ↑ PR
develop分支（测试配置）
  ↑ PR
feature分支（变更配置）
```

### 2.2 Jinja2 模板

```jinja2
! 交换机配置模板
hostname {{ hostname }}
!
{% for vlan in vlans %}
vlan {{ vlan.id }}
  name {{ vlan.name }}
{% endfor %}
!
{% for iface in interfaces %}
interface {{ iface.name }}
  description {{ iface.description }}
  switchport mode {{ iface.mode }}
{% if iface.vlan %}
  switchport access vlan {{ iface.vlan }}
{% endif %}
{% endfor %}
```

### 2.3 Ansible 网络自动化

```yaml
- name: Configure access switches
  hosts: access_switches
  gather_facts: false
  tasks:
    - name: Apply VLAN config
      cisco.ios.ios_config:
        src: templates/vlan_config.j2
        backup: yes
      notify: save_config

  handlers:
    - name: save_config
      cisco.ios.ios_command:
        commands: write memory
```

## 3. 网络CI/CD

### 3.1 变更流水线

```
代码提交 → 语法检查 → 模拟验证 → 预发布部署 → 生产部署
```

### 3.2 Batfish 验证

```python
from pybatfish.client.commands import bf_session, bf_init_snapshot

bf_session.host = "batfish"
bf_init_snapshot("network_configs/")

# 验证路由
answer = bf.q.routes().answer()
# 验证ACL
answer = bf.q.filterLineReachability().answer()
# 验证端到端连通性
answer = bf_q.reachability(pathConstraints=PathConstraints(
    startLocation="host1", endLocation="host2")).answer()
```

## 4. 自动化运维

### 4.1 配置合规检查

```python
from pyats import aetest
from pyats.topology import loader

class ComplianceTest(aetest.Testcase):
    @aetest.test
    def check_dns(self, device):
        output = device.execute('show running-config | include name-server')
        assert '8.8.8.8' in output, 'DNS server not configured'

    @aetest.test
    def check_ntp(self, device):
        output = device.execute('show ntp associations')
        assert 'ntp.example.com' in output, 'NTP not configured'
```

### 4.2 自动修复

```yaml
- name: Auto-remediate BGP sessions
  hosts: routers
  tasks:
    - name: Check BGP status
      cisco.ios.ios_command:
        commands: show bgp summary
      register: bgp_status

    - name: Reset BGP if needed
      cisco.ios.ios_command:
        commands: clear bgp * soft
      when: "'Idle' in bgp_status.stdout[0]"
```

## 参考文献

MDN HTTP 文档：https://developer.mozilla.org/zh-CN/docs/Web/HTTP
RFC 9110（HTTP 语义）：https://www.rfc-editor.org/rfc/rfc9110
TCP/IP 详解（W. Richard Stevens）：https://www.oreilly.com/library/view/tcpip-illustrated-vol/
Cloudflare 学习中心：https://www.cloudflare.com/learning/
DNS 原理（RFC 1035）：https://www.rfc-editor.org/rfc/rfc1035

## 延伸阅读

网络基础与协议，见 032-networking 模块文档。
网络安全（TLS/WAF），见 033-cybersecurity 模块。
负载均衡与网关，见 031-devops 模块相关文档。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供计算机网络课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 TCP 拥塞控制

慢启动：指数增长直到 ssthresh；拥塞避免：线性增长；快速重传/快速恢复处理丢包。
BBR（Google）基于带宽与延迟估计，替代丢包驱动的传统算法。
队列与缓冲膨胀（bufferbloat）导致延迟抖动；AQM（CoDel）缓解。
调优：理解 RTT、窗口与带宽延迟积（BDP）的关系。

### 13.2 HTTPS 与证书体系

TLS 握手：ClientHello -> ServerHello + 证书 -> 密钥交换 -> Finished；1.3 一轮往返完成。
证书链：根 CA -> 中间 CA -> 站点证书；OCSP/CRL 吊销检查。
Let's Encrypt 自动化签发与续期（ACME 协议）。
配置基线：TLS 1.2+、禁用弱套件、HSTS、证书透明度。
