<script lang="ts">
	import '../app.css';
	
	let { children } = $props();
</script>

<svelte:head>
	<title>U-Hilali</title>
</svelte:head>

{@render children()}
