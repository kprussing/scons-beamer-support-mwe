from pathlib import Path

from matplotlib import pyplot

fig, axs = pyplot.subplots(1, 1)
axs.plot([0, 1], [0, 1])

fig.savefig(Path(__file__).with_suffix(".png"))
