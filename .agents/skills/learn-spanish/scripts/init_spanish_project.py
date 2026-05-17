#!/usr/bin/env python3
"""Initialize a Castellano learning project from bundled templates."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = SKILL_DIR / "assets" / "templates"


FILES = {
    "learning-config.json": "learning-config.json",
    "state/progress.json": "progress.json",
    "state/vocabulary.json": "vocabulary.json",
    "state/errors.json": "errors.json",
    "notes/session-log.md": "session-log.md",
    "notes/grammar-notes.md": "grammar-notes.md",
    "notes/textbook-map.md": "textbook-map.md",
}


GITIGNORE = """# Local textbook material is available to the tutor but not tracked.
textbook/source/
textbook/extracted/
textbook/media/
textbook/workbook/

# Common source/media formats.
*.pdf
*.epub
*.mobi
*.azw3
*.doc
*.docx
*.mp3
*.m4a
*.wav
*.mp4
*.mov

# Temporary files.
.DS_Store
*.tmp
*.bak
"""


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=False)


def git_has_identity(cwd: Path) -> bool:
    name = run(["git", "config", "user.name"], cwd)
    email = run(["git", "config", "user.email"], cwd)
    return name.returncode == 0 and bool(name.stdout.strip()) and email.returncode == 0 and bool(email.stdout.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a Castellano learning project.")
    parser.add_argument("--path", default="./spanish-learning", help="Target project path. Defaults to ./spanish-learning.")
    args = parser.parse_args()

    project = Path(args.path).expanduser().resolve()
    project.mkdir(parents=True, exist_ok=True)

    for directory in [
        "state",
        "notes",
        "textbook/source",
        "textbook/extracted",
        "textbook/media",
        "textbook/workbook",
    ]:
        (project / directory).mkdir(parents=True, exist_ok=True)

    created: list[Path] = []
    skipped: list[Path] = []

    for target_name, template_name in FILES.items():
        target = project / target_name
        if target.exists():
            skipped.append(target.relative_to(project))
            continue
        shutil.copyfile(TEMPLATE_DIR / template_name, target)
        created.append(target.relative_to(project))

    gitignore = project / ".gitignore"
    if gitignore.exists():
        skipped.append(gitignore.relative_to(project))
    else:
        gitignore.write_text(GITIGNORE, encoding="utf-8")
        created.append(gitignore.relative_to(project))

    if not (project / ".git").exists():
        result = run(["git", "init"], project)
        if result.returncode != 0:
            print(result.stderr.strip() or "git init failed")
            return result.returncode

    if created:
        run(["git", "add", "learning-config.json", "state", "notes", ".gitignore"], project)
        diff = run(["git", "diff", "--cached", "--quiet"], project)
        if diff.returncode != 0:
            if git_has_identity(project):
                commit = run(["git", "commit", "-m", "Initialize Castellano learning project"], project)
                if commit.returncode != 0:
                    print(commit.stderr.strip() or "Initial git commit failed")
                    return commit.returncode
            else:
                print("Git identity is not configured; files were staged but not committed.")

    print(f"Project: {project}")
    if created:
        print("Created:")
        for path in created:
            print(f"  {path}")
    if skipped:
        print("Skipped existing:")
        for path in skipped:
            print(f"  {path}")
    if not created:
        print("No files created.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
