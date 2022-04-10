import src.shell as shell
import re

def __findField(fieldNames, coreData):
	for field_name in fieldNames:
		if field_name in coreData:
			return coreData[field_name]

def info():
	cpuinfo = shell.exec('cat /proc/cpuinfo')
	processors = re.split("\s?\n\s?\n", cpuinfo.strip())
	core = {}

	for processor in processors:
		details = re.split("\n", processor)
		for detail in details:
			detail = re.split("\s*:\s*", detail.strip())
			core[detail[0].lower()] = detail[1].strip()
		break

	info = {
		"model": __findField(['model name','cpu model','cpu','processor'], core),
		"frequency": __findField(['cpu mhz','clock'], core),
		"cache": __findField(['cache size','l2 cache'], core),
		"physicalCoreCount": int(__findField(['cpu cores'], core)),
		"coreCount": len(processors)
	}

	return info

def getMaxFrequency():
	frecuency = shell.exec('cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq')
	frecuency = round(int(frecuency.strip()) / 1000)

	if frecuency:
		return f"{frecuency} MHz"

	return ''
