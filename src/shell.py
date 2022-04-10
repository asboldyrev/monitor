import subprocess

def exec(command):
	result = subprocess.run([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

	if len(result.stderr) == 0:
		return result.stdout

	return ""
