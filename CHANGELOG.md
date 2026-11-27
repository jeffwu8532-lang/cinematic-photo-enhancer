# Changelog

## 0.2.0 — 2026-11-27 · Preview release / 预览版

- Added three original Chinese/English cinematic subtitle suggestions by default, based on each current photograph's content, lighting, setting, spatial relationships and visual mood.
- Separated chat suggestions from image placement: photo-only input yields an edited image without subtitles plus three suggestions. Add text only after an explicit selection or automatic-add request; skip suggestions and placement when declined.
- Added exact-selection follow-ups, automatic selection and placement, custom text, faithful translation, suggestion-only requests, per-image candidate tracking and ambiguous-reference handling.
- Subtitle placement/replacement uses the preserved finished image without subtitles, changes only text and does not rerun photography enhancement. Added text/visual checks, bounded correction and failure handling.
- Kept `references/prompt.md` byte-for-byte unchanged from v0.1.0 and retained the original subtitle styling instruction. Original preset SHA-256: `53d2509dbe9b311c6f8c9563a095363ea82963179f06c0d9018a7f81c391426b`.
- Updated SKILL.md, subtitle reference, Chinese/English READMEs, acceptance cases and packaging/release instructions to v0.2.0. Moved host compatibility requirements from frontmatter into the skill body for validator compatibility.
- Added a standard-library package validator for preset preservation, metadata, local references and ZIP/source integrity, plus description-based red-bridge night-portrait examples.
- Validation scope: local/static and archive checks only; runtime behavior, photo quality, text rendering, host compatibility and license selection remain pending. Distributed as a GitHub preview release; no installation or new license grant is performed.

## 0.1.0 — Draft

- Encapsulated the original Chinese cinematic photography preset without rewriting its core text.
- Added image-only interaction, optional subtitles, actual image-editing requirements, failure handling and quality checks.
- Added bilingual README, release instructions and acceptance tests.
- Pending: image-based testing, host compatibility verification, license selection and public release.
