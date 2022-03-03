r"""
This file reads in Emily Griffith's high- and low-Ia median sequences.
"""

import os
PATH = os.path.dirname(os.path.abspath(__file__))

def read():
	r"""
	Reads in the Griffith et al. (2021) [1]_ GALAH DR3 median sequences.

	.. Griffith et al. (2021), arxiv: 2110.06240
	"""
	# with open("%s/offsets.txt" % (PATH), 'r') as f:
	# 	while True:
	# 		line = f.readline()
	# 		if line == "":
	# 			break
	# 		elif line[0] == '#':
	# 			continue
	# 		elif line.split()[0] == "O":
	# 			offset = float(line.split()[1])
	# 			break
	# 		else:
	# 			pass
	with open("%s/medseq.lowIa.Fe.txt" % (PATH), 'r') as f:
		lowia = {
			"[fe/h]": [],
			"[mg/fe]": []
		}
		while True:
			line = f.readline()
			if line == "":
				break
			elif line[0] == '#':
				continue
			else:
				line = line.split()
				# [Fe/H] = [Fe/Mg] + [Mg/H]
				lowia["[fe/h]"].append(float(line[1]) + float(line[0]))
				# [O/Fe] = [O/Mg] - [Fe/Mg]
				# lowia["[o/fe]"].append(offset - float(line[1]))
				# [Mg/Fe] = -[Fe/Mg]
				lowia["[mg/fe]"].append(-float(line[1]))
		f.close()
	with open("%s/medseq.highIa.Fe.txt" % (PATH), 'r') as f:
		highia = {
			"[fe/h]": [],
			"[mg/fe]": []
		}
		while True:
			line = f.readline()
			if line == "":
				break
			elif line[0] == '#':
				continue
			else:
				line = line.split()
				# [Fe/H] = [Fe/Mg] + [Mg/H]
				highia["[fe/h]"].append(float(line[1]) + float(line[0]))
				# [O/Fe] = [O/Mg] - [Fe/Mg]
				# highia["[o/fe]"].append(offset - float(line[1]))
				# [Mg/Fe] = -[Fe/Mg]
				highia["[mg/fe]"].append(-float(line[1]))
	return lowia, highia


