#!/usr/bin/env python
"""Function to generate overlapping histograms"""

import random
import pathlib
import os
from matplotlib import pyplot as plt

# This script
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()

def gen_histograms(x, y, fig_size=(10, 5), plot_title="Distribution Comparison", title_size=16):
    f = plt.figure(figsize=fig_size)
    _, bins, _ = plt.hist(x, bins=50, range=[-6, 6])
    plt.hist(y, bins=bins, alpha=0.5)
    plt.title(plot_title, size=title_size)
    return(f)




# Tests
# Create sample distributions
sam_x = [random.gauss(3,1) for _ in range(400)]
sam_y = [random.gauss(4,2) for _ in range(400)]
# Run 
sample_figure = gen_histograms(x=sam_x, y=sam_y)
sample_figure.savefig(os.path.join(SCRIPT_DIR, 'sample_fig.png'), format='png')