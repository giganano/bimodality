r"""
This file declares the time-dependence of the infall history at a given radius
for a simple exponential.
"""

from ..._globals import END_TIME
from .utils import exponential
from .normalize import normalize_ifrmode
from .gradient import gradient


class expifr(exponential):

	def __init__(self, radius, dt = 0.01, dr = 0.1):
		# tau = 2 + radius / 2
		super().__init__(timescale = 6)
		self.norm *= normalize_ifrmode(self, gradient, radius, dt = dt, dr = dr)



