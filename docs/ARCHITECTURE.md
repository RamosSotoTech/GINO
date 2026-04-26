# Architecture Notes

This repository is structured to keep **engine/runtime concerns isolated** from
core gameplay decisions.

## Folder intent

- `src/gino/core/`: application lifecycle and bootstrap-level orchestration.
- `src/gino/entities/`: data-centric game objects/components.
- `src/gino/systems/`: behavior and logic processors.
- `src/gino/scenes/`: scene/state management.
- `src/gino/ui/`: menus/HUD/widgets.
- `src/gino/assets/`: static files (images, audio, fonts).
- `src/gino/utils/`: generic helpers that should not depend on PyGame.

## Transferability rule of thumb

When adding new code, ask:

1. Is this tied to PyGame APIs?
2. If yes, can it be isolated behind an adapter/module boundary?
3. If no, place it in systems/entities/utils so it can be reused.
