r"""
This file declares the time-dependence of the infall history at a given radius
under the early-burst model.
"""

from ..._globals import END_TIME
from .utils import double_exponential
from .normalize import normalize_ifrmode
from .gradient import gradient
import math as m
import os


class earlyburst(double_exponential):

	def __init__(self, radius, dt = 0.01, dr = 0.1):
		super().__init__(onset = 1, ratio = 0.1)
		self.first.timescale = 0.2
		self.second.timescale = 6
		prefactor = normalize_ifrmode(self, gradient, radius, dt = dt, dr = dr)
		self.first.norm *= prefactor
		self.second.norm *= prefactor
		# self.second.norm = 0
		# self.first.timescale = 6
		# prefactor = normalize_ifrmode(self, gradient, radius, dt = dt, dr = dr)
		# self.first.norm *= prefactor


