"""Application entry point.

Keep this file thin so it can be replaced easily if you switch from PyGame to
another rendering/runtime stack.
"""

from gino.core.game import Game
from gino.core.settings import load_config


def main() -> None:
    config = load_config()
    game = Game.from_config(config)
    game.run()


if __name__ == "__main__":
    main()
