import docker

def info():
	containers = []

	client = docker.from_env()
	for container in client.containers.list(all=True):
		image_name = ''

		if len(container.image.tags):
			image_name = container.image.tags[0]

		containers.append({
			'name': container.name,
			'state': container.status,
			'image': image_name,
			'created': container.attrs['Created'],
			'StartedAt': container.attrs['State']['StartedAt'],
			'FinishedAt': container.attrs['State']['FinishedAt'],
		})

	return containers