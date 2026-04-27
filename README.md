# GINO - Game Is Not Over

A small PyGame lab project for experimenting and having fun.

## Environment setup

### 1) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

### 3) Verify PyGame installation

```bash
python -c "import pygame; print(pygame.version.ver)"
```

If the command prints a version (for example `2.6.0`), your environment is ready.

### 4) Run the game

From the repository root:

```bash
python -m gino
```

After installing with `python -m pip install -e .`, you can also use:

```bash
gino
```

Avoid running from inside `src/gino` with `python -m main`. This project uses
the standard `src/` layout, so the package import root is `src`, not
`src/gino`.

## Runtime settings

GINO loads user settings from an operating-system config folder and falls back
to safe defaults when no file exists yet.

- Linux: `~/.config/gino/settings.json`
- macOS: `~/Library/Application Support/GINO/settings.json`
- Windows: `%APPDATA%\GINO\settings.json`

The current config shape lives in `src/gino/core/settings.py`. A future settings
scene can update a `GameConfig` object and call `save_config()`.

## Project structure

```text
.
├── docs/
│   └── ARCHITECTURE.md
├── src/
│   └── gino/
│       ├── assets/
│       │   ├── fonts/
│       │   ├── images/
│       │   └── sounds/
│       ├── core/
│       │   ├── game.py
│       │   └── settings.py
│       ├── entities/
│       ├── scenes/
│       ├── systems/
│       ├── ui/
│       ├── utils/
│       └── main.py
├── tests/
├── .gitlab-ci.yml
├── requirements.txt
└── README.md
```

### Why this layout?

The structure is made to learn PyGame while keeping concepts transferable:

- `core` owns runtime lifecycle.
- `entities` stores data-focused objects.
- `systems` stores behavior.
- `scenes` manages game states/screens.
- `ui` keeps interface concerns separate.
- `utils` keeps generic, engine-agnostic helpers.

## GitLab updates recommended

1. **Enable branch protection + merge request approvals** for `main`.
2. **Require passing pipeline** before merge (uses `.gitlab-ci.yml`).
3. **Add MR templates** (`.gitlab/merge_request_templates/`) for consistent reviews.
4. **Turn on Code Quality/SAST** in CI once the codebase grows.
5. **Use milestones + labels** (`feature`, `bug`, `refactor`, `learning`) to track progress.

## GitLab setup help

See `docs/GITLAB_SETUP.md` for step-by-step project settings in GitLab UI.
