import python.shell as shell

def info():
	info = shell.exec('grep \'cpu \' /proc/stat | awk \'{print ($2+$4)*100/($2+$4+$5)}\' | tr -d \\\\n')

	return {'utilization': float(info)}