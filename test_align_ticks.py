#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from twinx_tick_utils import align_twinx_ticks

def get_ticks(y1_lim, y2_lim, target_num_ticks, prefer):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.set_ylim(y1_lim[0], y1_lim[1])
    ax2.set_ylim(y2_lim[0], y2_lim[1])
    align_twinx_ticks(ax1, ax2, target_num_ticks, prefer)
    ticks1 = ax1.get_yticks()
    ticks2 = ax2.get_yticks()
    plt.close(fig)
    return ticks1, ticks2, y1_lim, y2_lim

# Test cases

# 1. Equal tick count with prefer='min'
ticks1, ticks2, _, _ = get_ticks((0, 10), (0, 100), 5, 'min')
assert len(ticks1) == len(ticks2) == 5, "Tick count mismatch for prefer='min'"

# 2. Equal tick count with prefer='max'
ticks1, ticks2, _, _ = get_ticks((-3, 3), (-50, 50), 7, 'max')
assert len(ticks1) == len(ticks2) == 7, "Tick count mismatch for prefer='max'"

# 3. Zero inclusion when range crosses zero
ticks1, ticks2, _, _ = get_ticks((-5, 5), (-100, 100), 5, 'min')
assert 0 in ticks1, "Zero not included in ticks1"
assert 0 in ticks2, "Zero not included in ticks2"

# 4. Uniform spacing of ticks
ticks1, ticks2, _, _ = get_ticks((0, 20), (0, 200), 6, 'min')
diffs1 = np.diff(ticks1)
diffs2 = np.diff(ticks2)
assert np.allclose(diffs1, diffs1[0]), "Ticks1 are not uniformly spaced"
assert np.allclose(diffs2, diffs2[0]), "Ticks2 are not uniformly spaced"

# 5. Alignment of tick positions
ticks1, ticks2, y1_lim, y2_lim = get_ticks((-2, 2), (-100, 100), 5, 'min')
y1_min, y1_max = y1_lim
y2_min, y2_max = y2_lim
pos1 = (ticks1 - y1_min) / (y1_max - y1_min)
pos2 = (ticks2 - y2_min) / (y2_max - y2_min)
assert np.allclose(pos1, pos2), "Tick positions are not aligned"

print("All tests passed!")
