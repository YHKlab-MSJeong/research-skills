#!/usr/bin/env python3
"""Copyable Nature-style starter; its CLI draws SYNTHETIC example data only.

    python nature_template.py --output-dir /tmp/figure-demo --width single

For research use, replace build_demo() with real data loading and plotting.
Use nature_rc(), figure_size(), and save_figure() inside mpl.rc_context().
No global style changes or figure output occur merely by importing this file.
"""

import argparse
import math
from pathlib import Path
import warnings

import matplotlib as mpl
from matplotlib import font_manager
from matplotlib.figure import Figure
import numpy as np


WIDTH_MM = {"single": 89.0, "double": 183.0}
COLORS = (
    "#0072B2", "#D55E00", "#009E73", "#CC79A7",
    "#E69F00", "#56B4E9", "#000000", "#F0E442",
)


def nature_rc():
    """Return local defaults, reporting font substitution without installing fonts."""
    available = {font.name for font in font_manager.fontManager.ttflist}
    choices = ("Arial", "Helvetica", "Liberation Sans", "DejaVu Sans")
    font = next((name for name in choices if name in available), None)
    if font is None:
        raise RuntimeError("No supported sans-serif font found; choose an installed font.")
    if font not in ("Arial", "Helvetica"):
        warnings.warn(
            f"Arial/Helvetica unavailable; using {font}. "
            "This is a local substitute, not a guarantee of journal compliance.",
            UserWarning,
            stacklevel=2,
        )
    return {
        "font.family": "sans-serif",
        "font.sans-serif": [font],
        "font.size": 7,
        "axes.labelsize": 7,
        "axes.titlesize": 7,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "axes.linewidth": 0.5,
        "xtick.major.width": 0.5,
        "ytick.major.width": 0.5,
        "xtick.minor.width": 0.5,
        "ytick.minor.width": 0.5,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "lines.linewidth": 0.7,
        "lines.markersize": 3,
        "axes.grid": False,
        "axes.facecolor": "white",
        "figure.facecolor": "white",
        "text.color": "black",
        "axes.edgecolor": "black",
        "axes.labelcolor": "black",
        "axes.titlecolor": "black",
        "xtick.color": "black",
        "ytick.color": "black",
        "axes.prop_cycle": mpl.cycler(color=COLORS),
        "image.cmap": "cividis",
        "legend.frameon": False,
        "legend.labelcolor": "black",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "text.usetex": False,
        "savefig.dpi": 450,
        "savefig.bbox": None,
        "savefig.transparent": False,
        "savefig.facecolor": "white",
    }


def figure_size(width="single", height_mm=60.0):
    """Return the final canvas size in inches; reject invalid main-figure heights."""
    if width not in WIDTH_MM:
        raise ValueError("width must be 'single' or 'double'")
    if not math.isfinite(height_mm) or not 0 < height_mm <= 170:
        raise ValueError("height_mm must be finite and in (0, 170]")
    return WIDTH_MM[width] / 25.4, height_mm / 25.4


def save_figure(fig, output_stem):
    """Save PDF and 450 dpi PNG without replacing existing files or symlinks.

    Call within the same rc_context as figure creation. The literal stem gets
    '.pdf' and '.png' appended; no input files are read or rewritten here.
    """
    stem = Path(output_stem)
    targets = tuple(Path(str(stem) + suffix) for suffix in (".pdf", ".png"))
    if any(path.exists() or path.is_symlink() for path in targets):
        raise FileExistsError(f"Output already exists; choose a new stem: {stem}")
    stem.parent.mkdir(parents=True, exist_ok=True)
    # Reserve both outputs before rendering, including against concurrent writers.
    handles = []
    try:
        for target in targets:
            handles.append(target.open("xb"))
        for handle, fmt in zip(handles, ("pdf", "png")):
            fig.savefig(handle, format=fmt, dpi=450, bbox_inches=None)
    except BaseException:
        for handle in handles:
            handle.close()
        # Only remove files reserved by this call, never a pre-existing target.
        for target in targets[:len(handles)]:
            target.unlink()
        raise
    finally:
        for handle in handles:
            handle.close()
    return targets


def build_demo(width="single", height_mm=60.0):
    """Build clearly labelled synthetic curves; substitute actual research data here."""
    fig = Figure(figsize=figure_size(width, height_mm), layout="constrained")
    ax = fig.subplots()
    x = np.linspace(0, 1, 21)
    ax.plot(x, np.exp(-2 * x), marker="o", label="Synthetic A")
    ax.plot(x, np.exp(-4 * x), marker="s", linestyle="--", label="Synthetic B")
    ax.set(xlabel="Control parameter (a.u.)", ylabel="Response (a.u.)", xlim=(-0.03, 1.03))
    ax.set_ylim(0, 1.05)
    ax.set_title("Synthetic example; not research data")
    ax.legend()
    return fig


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path,
                        help="Separate destination for synthetic_demo.pdf and .png")
    parser.add_argument("--width", choices=tuple(WIDTH_MM), default="single")
    parser.add_argument("--height-mm", type=float, default=60.0)
    args = parser.parse_args(argv)
    try:
        figure_size(args.width, args.height_mm)
        with mpl.rc_context(nature_rc()):
            fig = build_demo(args.width, args.height_mm)
            targets = save_figure(fig, args.output_dir / "synthetic_demo")
            print(f"Font: {mpl.rcParams['font.sans-serif'][0]}")
            print(f"Canvas: {WIDTH_MM[args.width]:g} x {args.height_mm:g} mm")
            for target in targets:
                print(target)
    except (ValueError, FileExistsError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
