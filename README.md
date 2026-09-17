# file-tidy

Organize a messy folder in one command.

`file-tidy` moves loose files into clean category subfolders — **Images, Documents, Videos, Music, Archives, Programs, Code** — so your Downloads folder stops being a junk drawer. It is a single Python file with **zero dependencies**: if Python runs on your computer, this works.

## Quick start

Requires Python 3.9 or newer. Nothing to install.

```bash
# Preview what would happen (nothing is moved)
python tidy.py ~/Downloads --dry-run

# Actually organize the folder
python tidy.py ~/Downloads
```

On Windows (Command Prompt) the Downloads folder is usually `%USERPROFILE%\Downloads`:

```bat
python tidy.py %USERPROFILE%\Downloads --dry-run
```

## Example

Before:

```
Downloads/
├── holiday-photo.jpg
├── invoice-2026-09.pdf
├── setup.exe
├── song.mp3
└── vacation.zip
```

After running `python tidy.py Downloads`:

```
Downloads/
├── Images/holiday-photo.jpg
├── Documents/invoice-2026-09.pdf
├── Programs/setup.exe
├── Music/song.mp3
└── Archives/vacation.zip
```

## What goes where

| Category   | Extensions                                                        |
| ---------- | ----------------------------------------------------------------- |
| Images     | `.jpg` `.png` `.gif` `.webp` `.svg` and more                       |
| Documents  | `.pdf` `.docx` `.xlsx` `.pptx` `.txt` `.md` `.csv` and more        |
| Videos     | `.mp4` `.mkv` `.mov` `.avi` `.webm`                               |
| Music      | `.mp3` `.wav` `.flac` `.m4a` and more                              |
| Archives   | `.zip` `.rar` `.7z` `.tar` `.iso` and more                         |
| Programs   | `.exe` `.msi` `.dmg` `.apk` and more                               |
| Code       | `.py` `.js` `.html` `.css` `.json` and more                        |
| Others     | anything not recognized                                           |

## Safety first

- **Try `--dry-run` first** — it prints every move it would make and touches nothing.
- **Never overwrites** — if `Images/` already has `photo.jpg`, the new one becomes `photo (1).jpg`.
- Hidden files (starting with `.`) are left alone, and the script never moves itself.

## Roadmap

- [ ] `--undo` to reverse the last run
- [ ] Custom categories and rules from a config file
- [ ] Optional date-based renaming for photos

Ideas and pull requests are welcome — see [Contributing](#contributing).

## Contributing

This is a beginner-friendly project: the whole program is one small file (`tidy.py`) with tests in `tests/`. Run the tests with:

```bash
python -m unittest discover tests
```

## License

[MIT](LICENSE)
