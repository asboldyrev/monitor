<template>
	<div class="card">
		<div class="card-header">
			<div class="card-title h3">Память</div>
		</div>
		<table class="table table-striped table-hover">
			<tbody>
				<tr>
					<td>Всего</td>
					<td>{{ total }}</td>
				</tr>
				<tr>
					<td>Использовано</td>
					<td>{{ used }}</td>
				</tr>
				<tr>
					<td>Свободно</td>
					<td>{{ free }}</td>
				</tr>
			</tbody>
		</table>

		<div class="card-body">
			<div class="bar my-2">
				<div
					class="bar-item"
					role="progressbar"
					:class="classBarUsed()"
					:style="{ width: percent + '%'}"
				><span v-if="roundPercent > 10">{{ roundPercent }} %</span></div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				total: 'N.A.',
				used: 'N.A.',
				free: 'N.A.',
				percent: 0
			}
		},
		computed: {
			roundPercent() {
				return Math.round(this.percent);
			}
		},
		methods: {
			update() {
				fetch(
					'/json/memory.json',
					{
						headers: {
							'Content-Type': 'application/json;charset=utf-8'
						}
					}
				)
				.then(response => response.json())
				.then(result => {
					this.total = result.total;
					this.used = result.used;
					this.free = result.free;
					this.percent = result.percent;

					setTimeout(this.update, 60000);
				});
			},
			classBarUsed() {
				if(this.roundPercent < 50) {
					return 'bg-success';
				}

				if(this.roundPercent < 75) {
					return 'bg-warning';
				}

				return 'bg-error';
			}
		},
		beforeMount() {
			this.update();
		},
	}
</script>
