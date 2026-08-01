/**
 * 站点级常量定义
 * 定义 FANDEX 站点的元信息（标题、副标题、URL、作者、语言），
 * 供 SEO、Layout、Footer 等场景统一引用。
 */
import { RUNTIME } from '@/config/runtime';

export const SITE = {
  title: 'FANDEX',
  subtitle: '循序渐进',
  url: RUNTIME.siteUrl,
  author: 'fanquanpp',
  lang: 'zh-CN',
};
