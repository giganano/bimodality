
from vice.toolkit import J21_sf_law
import numbers

class tophat_burst(J21_sf_law):

	def __init__(self, area, onset, duration, factor, **kwargs):
		super().__init__(area, **kwargs)
		self.onset = onset
		self.duration = duration
		self.factor = factor

	def __call__(self, time, arg2):
		# result = super().__call__(time, arg2)
		if self.onset <= time <= self.onset + self.duration:
			# result /= self.factor
			return 0.5
		else:
			return 5
		# return result

	@property
	def onset(self):
		r"""
		Type : ``float``

		The time of onset of the top-hat burst
		"""
		return self._onset

	@onset.setter
	def onset(self, value):
		if isinstance(value, numbers.Number):
			if value >= 0:
				self._onset = float(value)
			else:
				raise ValueError("Onset must be non-negative.")
		else:
			raise TypeError("Onset must be a numerical value. Got: %s" % (
				type(value)))

	@property
	def duration(self):
		r"""
		Type : ``float``

		The duration of the top-hat burst
		"""
		return self._duration

	@duration.setter
	def duration(self, value):
		if isinstance(value, numbers.Number):
			if value >= 0:
				self._duration = float(value)
			else:
				raise ValueError("Duration must be non-negative.")
		else:
			raise TypeError("Duration must be a real number. Got: %s" % (
				type(value)))

	@property
	def factor(self):
		r"""
		Type : ``float``

		The factor by which the SFE timescale will decrease relative to the
		Johnson et al. (2021) prescription.
		"""
		return self._factor

	@factor.setter
	def factor(self, value):
		if isinstance(value, numbers.Number):
			if value > 0:
				self._factor = float(value)
			else:
				raise ValueError("Factor must be positive.")
		else:
			raise TypeError("Factor must be a real number. Got: %s" % (
				type(value)))

