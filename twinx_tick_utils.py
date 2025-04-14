
import numpy as np
from matplotlib.ticker import MaxNLocator

def _nice_ticks(vmin, vmax, num_ticks):
    locator = MaxNLocator(nbins=num_ticks - 1, steps=[1, 2, 2.5, 5, 10])
    ticks = locator.tick_values(vmin, vmax)
    return ticks

def _fit_tick_count(ticks, num_ticks, must_include_zero):
    ticks = np.array(ticks)
    step = ticks[1] - ticks[0]

    if must_include_zero and not np.any(np.isclose(ticks, 0)):
        n_left = int(np.ceil((ticks[0] - 0) / step))
        n_right = int(np.ceil((0 - ticks[-1]) / step))
        ticks = np.arange(-n_left * step, (n_right + 1) * step + step / 2, step)

    if len(ticks) < num_ticks:
        while len(ticks) < num_ticks:
            left = ticks[0] - step
            right = ticks[-1] + step
            if (num_ticks - len(ticks)) % 2 == 1:
                ticks = np.append(ticks, right)
            else:
                ticks = np.insert(ticks, 0, left)

    elif len(ticks) > num_ticks:
        center = 0 if must_include_zero else np.mean(ticks)
        idx_center = np.argmin(np.abs(ticks - center))
        half = num_ticks // 2
        idx_start = max(0, idx_center - half)
        idx_end = idx_start + num_ticks
        if idx_end > len(ticks):
            idx_end = len(ticks)
            idx_start = idx_end - num_ticks
        ticks = ticks[idx_start:idx_end]

    return ticks

def align_twinx_ticks(ax1, ax2, target_num_ticks=7, prefer='min'):
    y1_min, y1_max = ax1.get_ylim()
    y2_min, y2_max = ax2.get_ylim()

    y1_ticks = _nice_ticks(y1_min, y1_max, target_num_ticks)
    y2_ticks = _nice_ticks(y2_min, y2_max, target_num_ticks)

    if prefer == 'max':
        num_ticks = max(len(y1_ticks), len(y2_ticks))
    else:
        num_ticks = min(len(y1_ticks), len(y2_ticks))

    must_zero_y1 = y1_min < 0 < y1_max
    must_zero_y2 = y2_min < 0 < y2_max

    y1_final = _fit_tick_count(y1_ticks, num_ticks, must_zero_y1)
    y2_final = _fit_tick_count(y2_ticks, num_ticks, must_zero_y2)

    ax1.set_yticks(y1_final)
    ax2.set_yticks(y2_final)
    ax1.grid(True)
    ax2.grid(False)
