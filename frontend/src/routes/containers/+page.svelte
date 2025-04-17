<script lang="ts">
	import ContainerCard from '$lib/components/ContainerCard.svelte';
  import pihole from "$lib/assests/pihole.svg"
  import portainer from "$lib/assests/portainer.png"
  import Button from "$lib/components/Button.svelte"
  let test = [{name: "name", info: {status: "Running"}},{name: "na", info: {status: "Running"}},{name: "pi", info: {status: "Running"}} ]
</script>

<section class="w-[80%] m-auto mt-[20px]">
  <div class="flex justify-between">
  <b><h1 class="text-[1.5rem] m-[15px]">Containers</h1></b>
  <a href="/containers/create"><Button content="Create Contianer"/></a>
  </div>
  <div class="flex flex-wrap">
  {#each test as item}
  <ContainerCard img={pihole} name={item.name} status={item.info.status} />
  {/each}
  </div>
</section>
