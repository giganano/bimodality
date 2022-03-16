r"""
Ensures runtime dependencies are satisfied for producing figures in Johnson et
al. (2021).

Dependencies:

	- matplotlib >= 2.0.0
	- NumPy >= 1.17.0
"""

try:
	ModuleNotFoundError
except NameError:
	ModuleNotFoundError = ImportError

# Enforce matplotlib >= 2.0.0 or else RuntimeError
try:
	import matplotlib as mpl
except (ModuleNotFoundError, ImportError):
	raise ModuleNotFoundError("Matplotlib not found.")
if tuple([int(i) for i in mpl.__version__.split('.')])[:2] < (2, 0):
	raise RuntimeError("""Matplotlib version >= 2.0.0 required for producing \
Johnson et al. (2021) figures. Current: %s""" % (mpl.__version__))
else: pass

# Enforce NumPy >= 1.17.0 or else RuntimeError
try:
	import numpy as np
except (ModuleNotFoundError, ImportError):
	raise ModuleNotFoundError("NumPy not found.")
if tuple([int(i) for i in np.__version__.split('.')])[:2] < (1, 17):
	raise RuntimeError("""NumPy version >= 1.17.0 required for producing \
Johnson et al. (2021) figures. Current: %s""" % (np.__version__))
else: pass


# Text parameters
# mpl.rcParams["font.family"] = "serif"
# mpl.rcParams["text.usetex"] = True
# mpl.rcParams["mathtext.fontset"] = "custom"
# mpl.rcParams["text.latex.preamble"] = r"\usepackage{amsmath}"
# mpl.rcParams["figure.titlesize"] = 18
# mpl.rcParams["axes.titlesize"] = 18
# mpl.rcParams["axes.labelsize"] = 20
# mpl.rcParams["xtick.labelsize"] = 18
# mpl.rcParams["ytick.labelsize"] = 18
# mpl.rcParams["legend.fontsize"] = 18

# # Figure formatting
# mpl.rcParams["figure.figsize"] = (5, 5)
# mpl.rcParams["figure.facecolor"] = "white"

# # Error bars and legend formatting
# mpl.rcParams["errorbar.capsize"] = 5
# mpl.rcParams["legend.numpoints"] = 1
# mpl.rcParams["legend.frameon"] = False
# mpl.rcParams["legend.handletextpad"] = 0.3

# # Axes and tick formatting
# mpl.rcParams["axes.linewidth"] = 0.75
# mpl.rcParams["xtick.direction"] = "in"
# mpl.rcParams["ytick.direction"] = "in"
# mpl.rcParams["ytick.right"] = True
# mpl.rcParams["xtick.top"] = True
# mpl.rcParams["xtick.minor.visible"] = True
# mpl.rcParams["ytick.minor.visible"] = True
# mpl.rcParams["xtick.major.size"] = 10
# mpl.rcParams["ytick.major.size"] = 10
# mpl.rcParams["xtick.minor.size"] = 5
# mpl.rcParams["ytick.minor.size"] = 5
# mpl.rcParams["xtick.major.width"] = 0.5
# mpl.rcParams["ytick.major.width"] = 0.5
# mpl.rcParams["xtick.minor.width"] = 0.5
# mpl.rcParams["ytick.minor.width"] = 0.5

