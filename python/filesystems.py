import psutil
import python.helpers as helpers

def info():
	info = []

	for disk in psutil.disk_partitions():
		disk_usage = psutil.disk_usage(disk.mountpoint)
		info.append({
			'total': helpers.bytes_convert(disk_usage.total, precission=2),
			'used': helpers.bytes_convert(disk_usage.used, precission=2),
			'free': helpers.bytes_convert(disk_usage.free, precission=2),
			'percent': f"{disk_usage.percent} %",
			'type': disk.fstype,
			'mount': disk.mountpoint,
			'filesystem': disk.device,
		})

	return info