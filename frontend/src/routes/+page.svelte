<script lang="ts">
	import Card from '$lib/components/Card.svelte';
  import Chart from "$lib/components/Chart.svelte"
  import container from "$lib/assests/container.png"
  import network from "$lib/assests/network.png"
  import image from "$lib/assests/images.png"
  let {data} = $props()
console.log(data)
</script>

<section class="w-[80%] m-auto mt-[20px]">
  <b><h1 class="text-[1.5rem] m-[15px]">Environment</h1></b>
  <div class="flex flex-wrap justify-between">
  <Card title="Containers" img={container} amount={data.container_info.containers}/>
  <Card title="Networks" img={network} amount={data.container_info.networks}/>
  <Card title="Images" img={image} amount={data.container_info.images}/>
  </div>
  <Chart/>
</section>
