import json
import python.cpu as cpu
import python.system as system
import python.memory as memory
import python.average as average
import python.filesystems as filesystems
import python.docker as docker
import python.utilization as utilization

cpu_info = cpu.info()
with open('./json/cpu.json', 'w') as file:
    json.dump(cpu_info, file)

system_info = system.info()
with open('./json/system.json', 'w') as file:
    json.dump(system_info, file)

memory_info = memory.info()
with open('./json/memory.json', 'w') as file:
    json.dump(memory_info, file)

average_info = average.info()
with open('./json/average.json', 'w') as file:
    json.dump(average_info, file)

filesystems_info = filesystems.info()
with open('./json/filesystems.json', 'w') as file:
    json.dump(filesystems_info, file)

docker_info = docker.info()
with open('./json/docker.json', 'w') as file:
    json.dump(docker_info, file)

utilization_info = utilization.info()
with open('./json/utilization.json', 'w') as file:
    json.dump(utilization_info, file)