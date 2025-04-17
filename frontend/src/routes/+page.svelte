<script lang="ts">
	import Card from '$lib/components/Card.svelte';
  import Chart from "$lib/components/Chart.svelte"
  import container from "$lib/assests/container.png"
  import network from "$lib/assests/network.png"
</script>

<section class="w-[80%] m-auto mt-[20px]">
  <b><h1 class="text-[1.5rem] m-[15px]">Environment</h1></b>
  <div class="flex flex-wrap justify-between">
  <Card img={container} amount={5}/>
  <Card img={network} amount={1}/>
  <Card img={network} amount={1}/>
  </div>
  <Chart/>
</section>
