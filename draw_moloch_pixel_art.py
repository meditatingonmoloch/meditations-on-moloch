#!/usr/bin/env python3
"""Draw a small Moloch-inspired pixel art figure."""

from __future__ import annotations

import argparse
from pathlib import Path


PALETTE = {
    ".": (0, 0, 0),
    " ": (0, 0, 0),
    "r": (96, 18, 18),
    "R": (178, 34, 34),
    "o": (226, 88, 34),
    "y": (255, 190, 64),
    "b": (55, 38, 28),
    "B": (111, 78, 55),
    "s": (135, 135, 135),
    "S": (205, 205, 205),
    "w": (238, 232, 213),
}

PIXELS = [
    ".........................",
    "..........y...y..........",
    ".........yo...oy.........",
    "........yoo...ooy........",
    ".......yoR.....Roy.......",
    "......yoRR.....RRoy......",
    ".....yoRRR.....RRRoy.....",
    ".....oRRRRRRRRRRRRo......",
    "....oRRRRRRRRRRRRRRo.....",
    "...oRRRwwRRRRRwwRRRRo....",
    "...RRRRwwRRRRRwwRRRRR....",
    "..RRRRRRRRRooRRRRRRRRR...",
    "..RRRRRRRRooooRRRRRRRR...",
    "..RRRRRRRRRooRRRRRRRRR...",
    "...RRRRRsssssssRRRRR.....",
    "...RRRRsSSSSSSSsRRRR.....",
    "....RRRsSBBBBBsSRRR......",
    ".....RRsSBBBBBsSRR.......",
    "......RsSBBBBBsSR........",
    ".......sSBBBBBsS.........",
    "......bSSBBBBBSSb........",
    ".....bbBSSSSSSSBbb.......",
    "....bbbBBsssssBBbbb......",
    "...bbbbBB.....BBbbbb.....",
    "..bbbbBB.......BBbbbb....",
    ".........................",
]


def ansi_block(rgb: tuple[int, int, int]) -> str:
    red, green, blue = rgb
    return f"\033[48;2;{red};{green};{blue}m  \033[0m"


def draw_terminal() -> None:
    for row in PIXELS:
        print("".join(ansi_block(PALETTE[pixel]) for pixel in row))


def save_ppm(path: Path, scale: int) -> None:
    width = len(PIXELS[0]) * scale
    height = len(PIXELS) * scale
    rows: list[str] = [f"P3\n{width} {height}\n255\n"]

    for row in PIXELS:
        expanded_pixels = []
        for pixel in row:
            expanded_pixels.extend([PALETTE[pixel]] * scale)
        line = " ".join(f"{r} {g} {b}" for r, g, b in expanded_pixels)
        rows.extend([line + "\n"] * scale)

    path.write_text("".join(rows), encoding="ascii")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Draw Moloch pixel art in the terminal or save it as PPM."
    )
    parser.add_argument(
        "--save",
        type=Path,
        help="Optional output path for a PPM image, for example moloch.ppm.",
    )
    parser.add_argument(
        "--scale",
        type=int,
        default=12,
        help="Pixel scale for saved PPM output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    draw_terminal()

    if args.save:
        if args.scale < 1:
            raise SystemExit("--scale must be at least 1")
        save_ppm(args.save, args.scale)
        print(f"\nSaved {args.save}")


if __name__ == "__main__":
    main()
