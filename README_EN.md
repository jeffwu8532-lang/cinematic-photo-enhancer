# CineFrame · Cinematic Photo Enhancer

Upload a photograph to reinterpret its lighting, color, optics and spatial storytelling, and receive three original bilingual cinematic subtitle suggestions tailored to that image.

**Version: v0.2.0 · GitHub preview release · Visual acceptance pending**

[GitHub repository](https://github.com/jeffwu8532-lang/cinematic-photo-enhancer) · [Download v0.2.0](https://github.com/jeffwu8532-lang/cinematic-photo-enhancer/releases/tag/v0.2.0)

[中文](README.md) · [Changelog](CHANGELOG.md) · [Acceptance tests](tests/test-cases.md) · [Packaging and release](PUBLISH.md)

## Features

- Preserve subject identity, proportions, framing, composition, perspective and scene semantics.
- Rebuild selective lighting, tonal hierarchy and a restrained warm/cool palette.
- Simulate optical depth, soft bloom and subtle halation, adapting to original day/night conditions and material properties.
- Create three original Chinese/English subtitle pairs from the current image's content, lighting, setting, spatial relationships and visual mood.
- Show suggestions separately. The default edited photograph has no added subtitles; selection or explicit automatic-add permission is required to place text on it.
- Skip both suggestions and placement when subtitles are explicitly declined. Support exact custom text and faithful translation when requested.

The original Chinese photography preset in [references/prompt.md](references/prompt.md) is byte-for-byte unchanged from v0.1.0. The update changes workflow and subtitle capabilities. Detailed rules are in [references/subtitles.md](references/subtitles.md).

## Usage

1. Install the entire `cinematic-photo-enhancer` folder in a host supporting Agent Skills and actual reference-image editing.
2. Invoke the skill, for example `$cinematic-photo-enhancer` where supported.
3. Attach the original photograph, either with the invocation or afterward. No preset selection or extra prompt is needed.
4. Receive the actual edited image without subtitles, followed by three numbered Chinese/English suggestions. Keep the image as delivered or select a suggestion.

| Request | Behavior |
|---|---|
| Photo only | Edit the image and separately suggest three pairs; place no text on the image |
| “Use option 2” | Add the exact pair from option 2 to its corresponding finished image |
| “Choose one automatically and add it” | Create three suggestions, select and add one, identify the choice; no further confirmation |
| “No subtitles” | Edit the image; skip both suggestions and placement |
| “Suggest captions, but don't put them on the image” | Edit and suggest three pairs separately |
| “Only suggest subtitles; do not edit the photo” | Read the current photo and suggest three pairs without image editing |
| “Add bilingual subtitles: 风从远方来 / The wind comes from afar.” | Use the supplied wording exactly instead of replacing it with a suggestion |

Adding or replacing subtitles uses the preserved finished image without subtitles as its base and produces a separate subtitled version. Do not rerun photography enhancement or change the subject, lighting or color. Each image in a batch has its own three suggestions and numbering. Clarify ambiguous image/option references. Permission to add automatically to one image does not silently extend to later images.

Suggestions express visual atmosphere without asserting a person's actual feelings or inventing identities, relationships or off-camera events. Write each set afresh rather than quoting film dialogue or reusing a caption library. Keep Chinese concise, use natural English adaptations and vary the narrative angle across the three options.

## Night portrait with a red bridge: examples

These examples use only the supplied description “night scene, red bridge, portrait.” The original photo pixels were unavailable for inspection; these are copy examples, not image-based test results.

1. **Color and space**  
   一抹桥红，让夜有了方向。  
   A trace of red gives the night a sense of direction.
2. **Figure and stillness**  
   灯火铺开，身影留在这一刻。  
   The lights stretch on; a figure holds this moment.
3. **Light and time**  
   夜色很深，这一帧刚好有光。  
   The night runs deep. This frame holds just enough light.

## Installation and validation

Place the complete folder in the user skill directory supported by the host, then reload and verify discovery. Back up an existing version before replacing the entire folder to avoid mixed versions. Building this package does not install or overwrite a skill.

Run these commands from the project folder with Python 3 (standard library only):

```bash
python3 tests/validate_package.py
python3 tests/validate_package.py --zip ../cinematic-photo-enhancer-v0.2.0.zip
```

The validator checks the original preset hash, version metadata, files, local links and archive/source equality. It does not call image services or prove runtime behavior. See the acceptance tests for behavioral and visual checks. Chinese workflow instructions and the original Chinese preset are used without translation to preserve the author's wording.

## Limitations and release status

This is a prompt-only skill, not an image model, editing engine or API service. It requires a host that can read and edit an attached reference image and return image output. Exact dimensions, identity preservation, local lighting and text rendering require visual validation. Generative text placement cannot guarantee unchanged pixels outside the subtitle area; preserve and compare the base image rather than claiming perfect locking. If image editing fails but the photo remains readable, provide suggestions with an explicit statement that the image edit was not completed.

This update includes no end-to-end image-tool testing or certification of a particular client. The skill does not request a separate API key when using host tools; host permissions, costs and data rules still apply. Licensing remains the author's decision; no redistribution permission or LICENSE is added. Do not commit private images or credentials.

This version is distributed through a GitHub Release; access follows the repository's visibility settings. Publication does not certify visual acceptance or list the skill in a host's plugin marketplace. See the [release guide](PUBLISH.md) and [Agent Skills specification](https://agentskills.io/specification).
