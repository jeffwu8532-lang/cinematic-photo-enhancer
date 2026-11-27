# CineFrame · 电影级摄影重构

> 上传一张照片，重新组织光影、色彩与空间，同时获得3条为这张照片创作的中英双语电影字幕推荐。

**版本：v0.2.0 · GitHub 预览版 · 实图验收待执行**

[GitHub 仓库](https://github.com/jeffwu8532-lang/cinematic-photo-enhancer) · [v0.2.0 版本下载](https://github.com/jeffwu8532-lang/cinematic-photo-enhancer/releases/tag/v0.2.0)

[English](README_EN.md) · [版本记录](CHANGELOG.md) · [测试用例](tests/test-cases.md) · [打包与发布说明](PUBLISH.md)

## 功能

- 保留原图主体身份、比例、画幅、构图、透视与场景语义。
- 局部明度控制、集中亮区与深暗色场，提炼自然的冷暖色彩关系。
- 模拟镜头焦平面、渐进失焦、Bloom 与 Halation，自适应原图昼夜及材质属性。
- 根据当前照片的内容、光影、场景、空间关系和视觉情绪，独立创作3条中英双语电影字幕。
- 推荐单独显示，默认成片不写字幕。选中某条或明确要求自动添加后，才在已完成的成片上排字。
- 明确拒绝字幕时，跳过推荐和添加；支持自定义文字和忠实补译。

原始摄影提示词 [references/prompt.md](references/prompt.md) 与 v0.1.0 逐字节一致；本次变更仅更新执行流程与字幕能力。字幕详见 [references/subtitles.md](references/subtitles.md)。

## 使用

1. 在支持 Agent Skills 且具备参考图编辑工具的宿主中安装整个 `cinematic-photo-enhancer` 目录。
2. 显式调用 `cinematic-photo-enhancer`（支持 `$` 技能语法的环境可使用 `$cinematic-photo-enhancer`）。
3. 上传原始照片，也可在调用时同时上传。无需填写提示词、选择风格或先确认字幕。
4. 默认获得实际无字幕成片和编号1–3的双语推荐。可保留无字幕版，也可继续选择添加。

| 你说 | 行为 |
|---|---|
| 只上传照片 | 处理图片，单独推荐3条，不写入图片 |
| 「用第2条」 | 在对应成片上添加第2条中英文，不重做摄影效果 |
| 「自动选一条并加上」 | 推荐3条并择一添加，注明采用的条目，不再确认 |
| 「不要字幕」 | 只处理图片，跳过推荐和添加 |
| 「不要加到图里，但给我推荐」 | 处理图片并给3条文字推荐，不写入 |
| 「只推荐字幕，不要处理照片」 | 仅看当前照片创作，不调用图像编辑 |
| 「添加双语字幕：风从远方来 / The wind comes from afar.」 | 使用指定文字，不替换为推荐 |

后续添加/更换字幕以保留的无字幕成片为基底，另交付字幕版；只加字，不重新处理人物、光影或色彩。多图逐张处理并各给3条，编号归属各图；指代不清时只澄清目标。一次性自动添加授权不自动延续到下一张图。

推荐依据可见画面营造的氛围，不断言人物真实心理，不编造身份、关系和照片外故事，不引用现成台词或固定字幕库。中文简洁，英文自然意译，三条采用不同叙事角度。

## 夜景红桥人像 · 字幕示例

以下仅依据「夜景、红桥、人像」描述创作，未检查原照片像素；作为文案示例，不代表实图测试通过。

1. **色彩与空间**  
   一抹桥红，让夜有了方向。  
   A trace of red gives the night a sense of direction.
2. **人物与留白**  
   灯火铺开，身影留在这一刻。  
   The lights stretch on; a figure holds this moment.
3. **光影与时间**  
   夜色很深，这一帧刚好有光。  
   The night runs deep. This frame holds just enough light.

## 安装

将解压后的完整目录放入宿主支持的用户技能目录，重新加载并检查是否可发现。已有同名版本时先备份，再整体替换，避免新旧文件混用；下载或发布版本包不会自动安装或覆盖现有技能。

目录应保留为：

```text
cinematic-photo-enhancer/
├── SKILL.md
├── README.md
├── README_EN.md
├── CHANGELOG.md
├── PUBLISH.md
├── .gitignore
├── references/
│   ├── prompt.md
│   └── subtitles.md
└── tests/
    ├── test-cases.md
    └── validate_package.py
```

## 检查

仅需 Python 3 标准库，在工程目录执行：

```bash
python3 tests/validate_package.py
python3 tests/validate_package.py --zip ../cinematic-photo-enhancer-v0.2.0.zip
```

检查原始提示词哈希、版本元数据、目录/引用和 ZIP 与源文件的一致性；不会调用图像服务，也不能替代行为及实图验收。具体交互场景见测试用例。

## 兼容性与限制

本项目是纯提示词 Agent Skill，不包含图像模型、独立图像引擎或 API。宿主须能读取照片并调用实际参考图编辑工具。人物身份、精确尺寸、局部光影及字幕正确率仍需实图验证。仅能生成式加字时，不能保证字幕区域外像素完全不变；技能要求保留成片并检查，不能宣称绝对锁定。图像处理失败而照片仍可读取时，可单独提供推荐并明确说明尚未完成图像处理。

本次版本不包含端到端图像工具测试或特定客户端兼容性认证。使用宿主内置工具时，本技能不另索取 API 密钥；宿主权限、费用和数据处理规则仍适用。项目授权协议仍待作者决定，不擅自新增 LICENSE 或开放再分发许可。请勿提交私人照片、客户资料或密钥。

## 规范与发布

[Agent Skills 规范](https://agentskills.io/specification) · [打包与发布说明](PUBLISH.md)。本版本通过 GitHub Release 分发，实际可见性以仓库设置为准。发布不代表已完成实图验收，也不自动上架任何宿主的插件市场。
