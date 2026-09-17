#!/usr/bin/env python3
"""tidy.py — organize a messy folder by moving files into category subfolders.

Usage:
    python tidy.py <folder>            # organize for real
    python tidy.py <folder> --dry-run  # preview what would move, change nothing
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".heic", ".tiff"},
    "Documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md", ".csv", ".rtf", ".odt"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm", ".wmv"},
    "Music": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso"},
    "Programs": {".exe", ".msi", ".dmg", ".pkg", ".apk", ".deb", ".appimage"},
    "Code": {".py", ".js", ".ts", ".html", ".css", ".json", ".xml", ".yml", ".yaml", ".sh", ".bat", ".ps1", ".java", ".c", ".cpp", ".rs", ".go"},
}

EXTENSION_MAP = {
    ext: category
    for category, extensions in CATEGORIES.items()
    for ext in extensions
}


def unique_destination(path: Path) -> Path:
    """Return path, or path with ' (1)', ' (2)'... appended if the name is taken."""
    stem, suffix, counter = path.stem, path.suffix, 1
    while path.exists():
        path = path.with_name(f"{stem} ({counter}){suffix}")
        counter += 1
    return path


def tidy(folder: Path, dry_run: bool = False) -> int:
    """Move loose files in folder into category subfolders. Returns the count."""
    script_path = Path(__file__).resolve()
    moved = 0
    for entry in sorted(folder.iterdir()):
        if not entry.is_file() or entry.name.startswith("."):
            continue
        if entry == script_path:
            continue
        category = EXTENSION_MAP.get(entry.suffix.lower(), "Others")
        destination = unique_destination(folder / category / entry.name)
        print(f"{entry.name}  ->  {category}/{destination.name}")
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(entry), str(destination))
        moved += 1
    return moved


def main() -> int:
    parser = argparse.ArgumentParser(description="Organize a messy folder by file type.")
    parser.add_argument("folder", type=Path, help="the folder to tidy, e.g. ~/Downloads")
    parser.add_argument("--dry-run", action="store_true", help="preview only; move nothing")
    args = parser.parse_args()

    folder = args.folder.expanduser().resolve()
    if not folder.is_dir():
        parser.error(f"not a folder: {folder}")

    moved = tidy(folder, dry_run=args.dry_run)
    verb = "Would move" if args.dry_run else "Moved"
    print(f"\n{verb} {moved} file{'s' if moved != 1 else ''}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
