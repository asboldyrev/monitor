import os
import psutil

def info():
	average = os.getloadavg()
	info = []
	core_count = psutil.cpu_count()

	for value in average:
		value = round((value * 100) / core_count)
		if (value > 100):
			value = 100
		info.append(value)

	return info