#!/usr/bin/env python
"""Function to generate overlapping histograms"""

import random
import pathlib
import os
from matplotlib import pyplot as plt
from typing import Final, Union, List
import pandas as pd

# This script location
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()

# Run preview
try:
    PREVIEW = os.getenv("PREVIEW", "False").lower() in ("true", "1", "t")
except:
    PREVIEW = False

# Handle list of numbers
Num = Union[int, float]


def gen_histograms(
    x: List[Num],
    y: List[Num],
    fig_size=(10, 5),
    plot_title="Actual vs. Synthetic Distribution",
    plot_suptitle="Distribution Comparison",
    title_size=16,
    show_grid=True,
    x_label="Feature Name",
    y_label="Count",
    show_bar_labels=True,
    legend_pos="upper right",
    labels=["Sample X", "Sample Y"],
):
    f = plt.figure(figsize=fig_size)
    _, bins, bars = plt.hist(
        x,
        bins=50,
        range=[min([*x, *y]), max([*x, *y])],
        label=labels[0],
        color="skyblue",
        lw=0,
    )
    plt.hist(y, bins=bins, alpha=0.5, label=labels[1], color="orange", lw=0)
    plt.title(plot_title, size=title_size - 3)
    plt.grid(show_grid)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if plot_suptitle is not None:
        plt.suptitle(plot_suptitle, size=title_size)
    if show_bar_labels:
        plt.bar_label(bars)
    if legend_pos is not None:
        plt.legend(loc=legend_pos)
    return f


# Tests
if PREVIEW:
    # Create sample distributions
    sam_x = [random.gauss(3, 1) for _ in range(400)]
    sam_y = [random.gauss(4, 2) for _ in range(400)]
    # Run
    sample_figure = gen_histograms(x=sam_x, y=sam_y)
    sample_figure.savefig(os.path.join(SCRIPT_DIR, "sample_fig.png"), format="png")


# Compare actual distributions
df_tabgan = pd.read_csv(
    os.path.join(SCRIPT_DIR, "..", "data", "fake", "tabgan_data.csv")
)
df_actual = pd.read_csv(os.path.join(SCRIPT_DIR, "..", "data", "raw", "train.csv"))

plt_compare = gen_histograms(
    x=random.sample(sorted(df_tabgan["Age"].values), 891),
    y=df_actual["Age"].values,
    plot_title="Synthetic and Real Age of Titanic Passengers",
    show_bar_labels=False,
    labels=['Synthetic', 'Actual'],
    x_label="Age"
)
plt_compare.savefig(
    os.path.join(SCRIPT_DIR, "tabgan_actual_comparison.png"), format="png"
)
