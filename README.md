# Castellano Learning Log

This repository tracks my Castellano learning progress using a textbook-led Codex tutor workflow.

The repo contains:

- learning progress and session notes
- structured local state for errors and textbook position
- the Codex skill used to guide lessons
- a textbook map for navigation

The textbook source file is intentionally not included.

## Current Textbook

Primary textbook:

```text
Colloquial Spanish
Untza Otaola Alday
```

The local PDF is expected under:

```text
textbook/source/
```

That folder is ignored by Git.

## Tutor Skill

The tutor behavior lives in:

```text
.agents/skills/learn-spanish/
```

The skill defines how lessons should work:

- textbook controls curriculum order
- Codex explains, drills, reviews, and tracks state
- progress is saved between sessions
- corrections focus on the current lesson target
- voice dictation and keyboard limitations are tolerated
- lesson timing is tracked lightly

## Repository Structure

```text
.
├── .agents/skills/learn-spanish/   # Codex tutor skill
├── learning-config.json            # Active textbook and project config
├── notes/
│   ├── grammar-notes.md
│   ├── session-log.md
│   └── textbook-map.md
├── state/
│   ├── errors.json
│   └── progress.json
└── textbook/
    └── source/                     # Local textbook files, ignored by Git
```

## Starting A Lesson

Open this repository in Codex and say:

```text
Use learn-spanish. Start my Castellano lesson.
```

For a short session:

```text
Use learn-spanish. I have 20 minutes. Continue my lesson.
```

## Notes

This is a personal learning repository, not a redistributed textbook package. The textbook file and other source media are kept local and ignored by Git.
