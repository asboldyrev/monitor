import python.shell as shell
import psutil
import re

__core = {}

def info():
	cpu_freq = int(psutil.cpu_freq()[2])

	cpu = {
		"model": __getBrand(),
		"frequency": f"{cpu_freq} MHz",
		"cache": __getCache(),
		"physicalCoreCount": psutil.cpu_count(False),
		"coreCount": psutil.cpu_count(),
	}

	return cpu

def __getBrand():
	return __findField([ 'model name', 'cpu model', 'cpu', 'processor' ])

def __getCache():
	return __findField([ 'cache size', 'l2 cache' ])

def __findField(fieldNames):
	if len(__core) == 0 :
		info = shell.exec('cat /proc/cpuinfo')
		processors = re.split("\s?\n\s?\n", info.strip())

		for processor in processors:
			details = re.split("\n", processor)
			for detail in details:
				detail = re.split("\s*:\s*", detail.strip())
				__core[detail[0].lower()] = detail[1].strip()
			break

	for field_name in fieldNames:
		if field_name in __core:
			return __core[field_name]