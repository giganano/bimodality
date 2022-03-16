
from vice.toolkit import J21_sf_law
import math as m
import numbers
from .models.utils import line, skewed_gaussian

class earlyburst(J21_sf_law):

	def __init__(self, area, timescale = 1, factor = 10, **kwargs):
		super().__init__(area, **kwargs)
		# self.duration = duration
		self.timescale = timescale
		self.factor = factor

	def __call__(self, time, arg2):
		result = (1 - m.exp(-time / self._timescale)) * super().__call__(time,
			arg2)
		if result < 0.2:
			return 0.2
		else:
			return result
		# if time <= self._duration:
		# 	# return super().__call__(time, arg2) / self._factor
		# 	return 0.2
		# else:
		# 	return super().__call__(time, arg2)

	# @property
	# def duration(self):
	# 	r"""
	# 	Type: ``float``

	# 	The duration of the early burst in Gyr.
	# 	"""
	# 	return self._duration

	# @duration.setter
	# def duration(self, value):
	# 	if isinstance(value, numbers.Number):
	# 		if value > 0:
	# 			self._duration = float(value)
	# 		else:
	# 			raise ValueError("Duration must be positive.")
	# 	else:
	# 		raise TypeError("Duration must be a real number. Got: %s" % (
	# 			type(value)))

	@property
	def timescale(self):
		r"""
		Type : ``float``

		The e-folding timescale on which SFE timescale approaches the
		Johnson et al. (2021) fiducial form
		"""
		return self._timescale

	@timescale.setter
	def timescale(self, value):
		if isinstance(value, numbers.Number):
			if value > 0:
				self._timescale = float(value)
			else:
				raise ValueError("Timescale must be positive.")
		else:
			raise TypeError("Timescale must be a real number. Got: %s" % (
				type(value)))

	@property
	def factor(self):
		r"""
		Type : ``float``

		The factor by which the fiducial Johnson et al. (2021) SFE timescale
		decreases at the beginning of the simulation. Length determined by
		the attribute ``duration``.
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


class gaussian_burst(J21_sf_law, skewed_gaussian):

	def __init__(self, area, mean = 2, amplitude = 0.5, std = 0.75, skew = 3,
			**kwargs):
		J21_sf_law.__init__(self, area, **kwargs)
		skewed_gaussian.__init__(self, mean = mean, amplitude = amplitude,
			std = std, skew = skew)

	def __call__(self, time, arg2):
		skewfac = 1 - skewed_gaussian.__call__(self, time)
		return skewfac * J21_sf_law.__call__(self, time, arg2)
		# return J21_sf_law.__call__(self, time, arg2)


class smoothed_tophat_burst(J21_sf_law):

	_RAMP_UP_ = 0.2
	_DURATION_ = 0.3
	_RAMP_DOWN_ = 0.7
	_BURST_MIN_TAUSTAR_ = 0.5

	def __init__(self, area, onset, **kwargs):
		super().__init__(area, **kwargs)
		self.onset = onset
		self.__duration = self._RAMP_UP_ + self._DURATION_ + self._RAMP_DOWN_

	def __call__(self, time, arg2):
		if self._onset <= time <= self._onset + self._RAMP_UP_:
			if hasattr(self, "rampup"):
				return self.rampup(time)
			else:
				self.rampup = line.from_points(
					[self._onset, super().__call__(time, arg2)],
					[self._onset + self._RAMP_UP_, self._BURST_MIN_TAUSTAR_])
				return self.rampup(time)
		elif (self._onset <= time <= self._onset +
			self._RAMP_UP_ + self._DURATION_):
			return self._BURST_MIN_TAUSTAR_
		elif (self._onset <= time <= self._onset +
			self._RAMP_UP_ + self._DURATION_ + self._RAMP_DOWN_):
			# print(time)
			if hasattr(self, "rampdown"):
				result = self.rampdown(time)
			else:
				# print(time)
				# print(time + self._RAMP_DOWN_)
				self.rampdown = line.from_points(
					[time, self._BURST_MIN_TAUSTAR_],
					[time + self._RAMP_DOWN_, super().__call__(
						time + self._RAMP_DOWN_, arg2)])
				print(self.rampdown.slope)
				print(self.rampdown.intercept)
				# quit()
				result = self.rampdown(time)
			print(result)
			return result
		else:
			return super().__call__(time, arg2)



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



class tophat_burst(J21_sf_law):

	def __init__(self, area, onset, duration, **kwargs):
		super().__init__(area, **kwargs)
		self.onset = onset
		self.duration = duration
		# self.factor = factor

	def __call__(self, time, arg2):
		# result = super().__call__(time, arg2)
		if self.onset <= time <= self.onset + self.duration:
			# result /= self.factor
			return 0.2 * super().__call__(time, arg2)
		else:
			return 2 * super().__call__(time, arg2)
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

	# @property
	# def factor(self):
	# 	r"""
	# 	Type : ``float``

	# 	The factor by which the SFE timescale will decrease relative to the
	# 	Johnson et al. (2021) prescription.
	# 	"""
	# 	return self._factor

	# @factor.setter
	# def factor(self, value):
	# 	if isinstance(value, numbers.Number):
	# 		if value > 0:
	# 			self._factor = float(value)
	# 		else:
	# 			raise ValueError("Factor must be positive.")
	# 	else:
	# 		raise TypeError("Factor must be a real number. Got: %s" % (
	# 			type(value)))

