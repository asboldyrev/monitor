<template>
	<div class="card" v-if="containers.length">
		<div class="card-header">
			<div class="card-title h3">Docker</div>
		</div>
		<table class="table table-striped table-hover">
			<thead>
				<tr>
					<th>Контайнер</th>
					<th>Статус</th>
					<th>Образ</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(container, index) in containers" :key="index">
					<td>
						<span class="badge" :class="{ 'badge-error': container.state != 'running' }">
							{{ container.name }}
						</span>
					</td>
					<td>{{ container.status }}</td>
					<td>{{ container.image }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
    const humanizeDuration = require("humanize-duration");

	export default {
		data() {
			return {
				containers: [],
			}
		},
		methods: {
			update() {
				fetch(
					'/json/docker.json',
					{
						headers: {
							'Content-Type': 'application/json;charset=utf-8'
						}
					}
				)
				.then(response => response.json())
				.then(result => {
					this.containers = [];
					result
						.sort((curr) => {
							return curr.state == 'running' ? -1 : 1
						})
						.forEach((item) => {
                            let diff;

                            if(item.state == 'running') {
                                diff = new Date(item.StartedAt) - Date.now();
                            } else {
                                diff = new Date(item.FinishedAt) - Date.now();
                            }
                            item.status = humanizeDuration(diff, { language: "ru", largest: 2, round: true });

                            this.containers.push(item);
                        });

					setTimeout(this.update, 300000);
				});
			}
		},
		beforeMount() {
			this.update();
		},
	}
</script>

<style scoped>
	.badge-error:after {
		background: #e85600;
	}
</style>
