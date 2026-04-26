"""Application entry point.

Keep this file thin so it can be replaced easily if you switch from PyGame to
another rendering/runtime stack.
"""

from gino.core.game import Game


def main() -> None:
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
