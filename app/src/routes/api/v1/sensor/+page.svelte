<script lang="ts">
	import { onMount } from 'svelte';

	let time = '';
	let temperature = '';
	let boron = '';
	let neutronFlux = '';

	let eventSource: EventSource;

	onMount(() => {
		eventSource = new EventSource('/api/v1/sensor');

		eventSource.onmessage = (event) => {
			const [t, temp, b, flux] = event.data.split(',');
			time = t;
			temperature = temp;
			boron = b;
			neutronFlux = flux;
		};

		return () => {
			eventSource.close();
		};
	});
</script>

<main class="p-10">
	<h1 class="mb-6 text-center text-2xl font-bold">Reactor Sensor Live Stream</h1>

	<div class="overflow-x-auto">
		<table class="table-zebra table-md bg-base-100 table rounded-lg shadow-md">
			<thead>
				<tr>
					<th class="text-base">ISO Time</th>
					<th class="text-base">Temperature (K)</th>
					<th class="text-base">Boron (ppm)</th>
					<th class="text-base">Neutron Flux</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>{time}</td>
					<td>
						<span class="badge badge-info badge-md">{temperature}</span>
					</td>
					<td>
						<span class="badge badge-accent badge-md">{boron}</span>
					</td>
					<td>
						<span class="badge badge-primary badge-md">{neutronFlux}</span>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</main>
