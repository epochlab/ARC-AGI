#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

cmap = [
    '#000000', # black
    '#0074D9', # blue
    '#FF4136', # red
    '#37D449', # green
    '#FFDC00', # yellow
    '#E6E6E6', # grey
    '#F012BE', # pink
    '#FF871E', # orange
    '#54D2EB', # light blue
    '#8D1D2C', # brown
    '#FFFFFF'
    ]

def plot_set(input_grids, output_grids):
    custom_cmap = ListedColormap(cmap)
    num_grids = len(input_grids)

    fig, ax = plt.subplots(num_grids, 2, figsize=(10, 5 * num_grids))
    fig.patch.set_facecolor('#292929')
    for i in range(num_grids):
        for j, grid in enumerate([input_grids[i], output_grids[i]]):
            ax[i, j].imshow(grid, cmap=custom_cmap, vmin=0, vmax=len(cmap) - 1)
            ax[i, j].set_title(f'{"Input" if j == 0 else "Output"} {i+1} | {grid.shape}', color='white')
            ax[i, j].set_xticks(np.arange(grid.shape[1] + 1) - 0.5, minor=True)
            ax[i, j].set_yticks(np.arange(grid.shape[0] + 1) - 0.5, minor=True)
            ax[i, j].grid(which='minor', color='white', linestyle='-', linewidth=0.5)
            ax[i, j].tick_params(axis='both', colors='white')

    plt.tight_layout(), plt.show()