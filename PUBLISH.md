# CineFrame v0.2.0 · 打包与发布说明

CineFrame 通过 GitHub 仓库与 Release 分发。当前版本为预览版，静态文件及压缩包可校验，行为与实图验收仍待执行。发布须在用户明确授权的范围内进行；可见性以仓库设置为准。

- 仓库：[jeffwu8532-lang/cinematic-photo-enhancer](https://github.com/jeffwu8532-lang/cinematic-photo-enhancer)
- 版本：[CineFrame v0.2.0](https://github.com/jeffwu8532-lang/cinematic-photo-enhancer/releases/tag/v0.2.0)
- 技能标识与目录：`cinematic-photo-enhancer`
- 版本元数据：`0.2.0`；Git 标签：`v0.2.0`
- 下载附件：`cinematic-photo-enhancer-v0.2.0.zip` 和 `SHA256SUMS`

## 发布内容

仓库根目录放置技能工程的10个源文件，便于读取 README 与 SKILL.md；Release ZIP 内保留一个顶层 `cinematic-photo-enhancer/` 目录，便于安装。ZIP 与 SHA256SUMS 作为 Release 附件，不混入技能目录。发布不会自动安装或覆盖现有技能。

原始摄影提示词必须与 v0.1.0 的 `references/prompt.md` 逐字节一致，SHA-256：

```text
53d2509dbe9b311c6f8c9563a095363ea82963179f06c0d9018a7f81c391426b
```

项目未新增开源授权协议；保留作者现有版权及授权说明。不要向仓库或附件加入私人照片、客户资料、密钥、本机路径记录或内部操作日志。

## 本地检查与打包

在技能工程目录执行：

```bash
python3 tests/validate_package.py
```

校验工具会忽略本地 Git 元数据，但仍拒绝其他额外源文件；ZIP 不允许包含 Git 元数据。检查必要文件、版本、原提示词哈希及本地 Markdown 引用成功后，在工程上一级执行以下 Python 3 脚本，按显式清单生成 ZIP：

```python
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path("cinematic-photo-enhancer")
files = [
    ".gitignore", "SKILL.md", "README.md", "README_EN.md",
    "CHANGELOG.md", "PUBLISH.md", "references/prompt.md",
    "references/subtitles.md", "tests/test-cases.md",
    "tests/validate_package.py",
]
with ZipFile("cinematic-photo-enhancer-v0.2.0.zip", "w", ZIP_DEFLATED) as archive:
    for relative in sorted(files):
        path = root / relative
        assert path.is_file() and not path.is_symlink(), path
        archive.write(path, path.as_posix())
```

返回工程目录复检：

```bash
python3 tests/validate_package.py --zip ../cinematic-photo-enhancer-v0.2.0.zip
```

检查 ZIP 的 CRC、目录与逐文件字节一致性。生成压缩包 SHA-256，写入同级 `SHA256SUMS`。任何内容变动都须重新打包、复检并更新校验和；已发布标签和附件不得静默替换，应以新版本说明后续变更。

## GitHub Release

在已授权的仓库中提交这10个文件，核对源文件后，为对应提交创建标签 `v0.2.0`。Release 标题为「CineFrame v0.2.0 — 智能双语字幕推荐」，标为预览版，并上传 ZIP 与 SHA256SUMS。

版本说明应包含：

- 默认上传即处理，并单独给3条原创中英双语字幕推荐。
- 选择或明确自动添加后才写入；明确拒绝则跳过推荐及添加。
- 在已完成的无字幕成片上仅加文字，不重跑摄影。
- 原始摄影提示词保持不变。
- 静态及 ZIP 检查已执行；40项行为/实图用例仍待真实宿主验收。

发布后核对标签指向正确提交、附件名称/大小/校验和与本地一致，以及 README 和字幕参考可以读取。对外公开须符合用户明确授权范围，不能仅凭完成本地工程就自行扩大可见性。

## 行为及实图验收

按 [tests/test-cases.md](tests/test-cases.md) 逐项执行。重点检查人物保真、昼夜、反射属性、原画幅，以及添加文字后画面是否保持。保留实际输入、成片、候选与所选字幕记录，不把静态检查或文案示例记为实图通过。

夜景红桥人像的3条示例仅根据场景描述创作，原照片像素未获检查。当前预览版不声称端到端兼容性或字幕渲染已经验证。GitHub 发布不会自动上架宿主的插件市场。
