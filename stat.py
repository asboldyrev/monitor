import json
import src.cpu as cpu

cpu_info = cpu.info()
max_frequency = cpu.getMaxFrequency()
cpu_info["frequency"] = max_frequency if max_frequency else cpu_info["frequency"]

with open('data.json', 'w') as file:
    json.dump({'cpuInfo': cpu_info}, file)
