from platform import platform
import platform
import python.shell as shell

def info():
	info = {
		'hostname': platform.node(),
		'system': __getSystemName(),
		'kernel': platform.release(),
		'uptime': float(shell.exec('cat /proc/uptime | awk \'{print $1}\' | tr -d \\\\n')),
		'timezone': shell.exec('timedatectl | grep "Time zone" | awk \'{print $3}\' | tr -d \\\\n'),
	}

	return info


def __getSystemName():
	name = shell.exec('/usr/bin/lsb_release -ds | cut -d= -f2 | tr -d \'"\'').strip()
	if name:
		return name

	name = shell.exec('cat /etc/system-release | cut -d= -f2 | tr -d \'"\'').strip()
	if name:
		return name

	name = shell.exec('find /etc/*-release -type f -exec cat {} \; | grep PRETTY_NAME | tail -n 1 | cut -d= -f2 | tr -d \'"\'').strip()
	if name:
		return name

	return ''