/**
 * 学习路径交互岛类型定义（客户端安全）
 * -----------------------------------------------------------------------------
 * 说明：仅定义类型，不引入任何服务端数据模块，避免客户端打包 doc-index 与地图 JSON。
 */
import type {
  KnowledgeDifficulty,
  KnowledgeOfficialLink,
} from '@fandex/utils/learning-path';
import type { OfficialDoc as ModuleOfficialDoc } from '@fandex/utils/modules';

/** 知识点节点视图模型 */
export interface NodeVM {
  id: string;
  title: string;
  desc?: string;
  difficulty?: KnowledgeDifficulty;
  stageId: string;
  stageTitle: string;
  href?: string;
  docTitle?: string;
  official?: KnowledgeOfficialLink;
}

/** 阶段视图模型 */
export interface StageVM {
  id: string;
  title: string;
  subtitle?: string;
  nodes: NodeVM[];
}

/** 技术视图模型 */
export interface TechVM {
  module: string;
  title: string;
  icon: string;
  summary: string;
  color: string;
  officialDocs: readonly ModuleOfficialDoc[];
  stages: StageVM[];
  stats: { stages: number; nodes: number; docs: number; gaps: number };
}

export type { KnowledgeDifficulty, KnowledgeOfficialLink };
