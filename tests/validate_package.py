#!/usr/bin/env python3
"""Validate CineFrame's local release files; no image-service calls or dependencies.

This checks the frontmatter subset used by this package, not arbitrary YAML.
Behavioral and visual acceptance still require a real host and photographs.
"""

import argparse
import hashlib
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


VERSION = "0.2.0"
SKILL_NAME = "cinematic-photo-enhancer"
ORIGINAL_PROMPT_SHA256 = (
    "53d2509dbe9b311c6f8c9563a095363ea82963179f06c0d9018a7f81c391426b"
)
PACKAGE_FILES = frozenset({
    ".gitignore", "SKILL.md", "README.md", "README_EN.md", "CHANGELOG.md",
    "PUBLISH.md", "references/prompt.md", "references/subtitles.md",
    "tests/test-cases.md", "tests/validate_package.py",
})


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_source(root):
    require(root.is_dir(), "Skill directory does not exist")
    paths = [p for p in root.rglob("*")
             if p.relative_to(root).parts[0] != ".git"]
    require(not any(p.is_symlink() for p in paths), "Symlinks are not allowed")
    actual = {p.relative_to(root).as_posix() for p in paths if p.is_file()}
    require(actual == PACKAGE_FILES,
            "File inventory mismatch: missing=%s, extra=%s" %
            (sorted(PACKAGE_FILES - actual), sorted(actual - PACKAGE_FILES)))
    contents = {name: (root / name).read_text(encoding="utf-8")
                for name in PACKAGE_FILES}
    print("PASS: 10-file inventory, UTF-8 readability, no extra files or symlinks (Git metadata excluded)")

    prompt_bytes = (root / "references/prompt.md").read_bytes()
    require(hashlib.sha256(prompt_bytes).hexdigest() == ORIGINAL_PROMPT_SHA256,
            "Original photography prompt differs from v0.1.0")
    print("PASS: photography prompt SHA-256 matches the v0.1.0 baseline")

    skill = contents["SKILL.md"]
    match = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    require(match is not None, "Missing or malformed frontmatter delimiters")
    # Fail closed if the maintained schema changes. Use a full YAML validator
    # separately when adding frontmatter fields or changing its representation.
    schema = re.fullmatch(
        r'name: (?P<name>[a-z0-9-]+)\n'
        r'description: >-\n(?P<description>(?:  [^\n]+\n)+)'
        r'metadata:\n  version: "(?P<version>[^"\n]+)"', match.group(1))
    require(schema is not None, "Frontmatter does not match the supported schema")
    require(schema.group("name") == SKILL_NAME, "Unexpected skill name")
    require(schema.group("version") == VERSION, "Unexpected skill version")
    description = " ".join(s.strip() for s in schema.group("description").splitlines())
    require(0 < len(description) <= 1024, "Invalid description length")
    require("<" not in description and ">" not in description,
            "Angle brackets in description")
    require("[TODO:" not in skill, "Unfinished skill scaffold")
    for name in ("README.md", "README_EN.md", "PUBLISH.md",
                 "references/subtitles.md", "tests/test-cases.md"):
        require("v" + VERSION in contents[name], "Missing current version in " + name)
    headings = re.findall(r"^## ([0-9]+\.[0-9]+\.[0-9]+)\b",
                          contents["CHANGELOG.md"], re.MULTILINE)
    require(bool(headings) and headings[0] == VERSION,
            "Changelog does not lead with current version")
    print("PASS: skill metadata schema, name, version and current document versions")

    link_count = 0
    for name, content in sorted(contents.items()):
        if not name.endswith(".md"):
            continue
        for target in re.findall(r"!?\[[^\]\n]*\]\(([^\s)]+)\)", content):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            if not url.path:
                continue
            resolved = ((root / name).parent / unquote(url.path)).resolve()
            require(resolved == root or root in resolved.parents,
                    "Local reference escapes skill directory: " + target)
            require(resolved.exists(), "Broken local link in %s: %s" % (name, target))
            link_count += 1
    print("PASS: %d local Markdown references resolve (external URLs not fetched)" % link_count)

    ids = re.findall(r"^\| (T\d+) \|", contents["tests/test-cases.md"], re.MULTILINE)
    require(ids == ["T%02d" % i for i in range(1, 41)],
            "Acceptance case IDs must be unique and ordered T01-T40")
    print("PASS: 40 acceptance scenarios indexed (runtime outcomes not evaluated)")


def check_archive(root, archive_path):
    expected = {SKILL_NAME + "/" + name for name in PACKAGE_FILES}
    with zipfile.ZipFile(archive_path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        require(len(names) == len(set(names)), "Duplicate archive entries")
        for info in infos:
            path = PurePosixPath(info.filename)
            require(not path.is_absolute() and ".." not in path.parts
                    and "\\" not in info.filename,
                    "Unsafe archive path: " + info.filename)
            require(not stat.S_ISLNK(info.external_attr >> 16),
                    "Archive contains symlink: " + info.filename)
        require(set(names) == expected,
                "Archive must contain exactly the 10 source files under one skill folder")
        require(archive.testzip() is None, "Archive CRC check failed")
        for name in sorted(PACKAGE_FILES):
            require(archive.read(SKILL_NAME + "/" + name) == (root / name).read_bytes(),
                    "Archive/source byte mismatch: " + name)
    print("PASS: ZIP paths, inventory, CRC and all 10 source-file byte comparisons")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--zip", dest="archive", type=Path)
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        check_source(root)
        if args.archive:
            check_archive(root, args.archive)
    except (OSError, UnicodeError, ValueError, zipfile.BadZipFile, RuntimeError) as exc:
        print("FAIL: " + str(exc), file=sys.stderr)
        return 1
    print("Static validation passed. Image-tool behavior and visual quality remain untested.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
