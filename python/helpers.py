def bytes_convert(bytes, format = '', precission = 0):
	#bytes = float(bytes)
	base = 1024
	units = [ 'B', 'KB', 'MB', 'GB', 'TB' ]

	if (len(format) == 0):
		index = len(units) - 1
		size = bytes
		while (bytes <= size):
			size = base ** index

			format = units[index]
			index -= 1
	else:
		format = format.upper()
		exp = units.index(format)
		size = base ** exp

	bytes = round(bytes / size, precission)

	return f"{bytes} {format}"