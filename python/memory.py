import psutil
import python.helpers as helpers

def info():
	stat = psutil.virtual_memory()

	total = helpers.bytes_convert(stat.total, precission=2)
	used = helpers.bytes_convert(stat.used, precission=2)
	free = helpers.bytes_convert(stat.available, precission=2)
	percent = round((stat.used * 100) / stat.total)

	info = {
		'total': total,
		'used': used,
		'free': free,
		'percent': f"{percent} %",
	}

	return info