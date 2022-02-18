
from ..._globals import END_TIME
from .utils import constant
from .normalize import normalize_ifrmode
from .gradient import gradient


class constifr(constant):

	def __init__(self, radius, amplitude = 1, dt = 0.01, dr = 0.1):
		super().__init__(amplitude = amplitude)
		self.amplitude *= normalize_ifrmode(self, gradient, radius,
			dt = dt, dr = dr)



