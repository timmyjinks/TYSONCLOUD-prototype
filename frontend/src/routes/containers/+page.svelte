<script lang="ts">
  import {seletectedContainer} from "$lib/store"
	import ContainerCard from '$lib/components/ContainerCard.svelte';
  import pihole from "$lib/assests/pihole.svg"
  import Button from "$lib/components/Button.svelte"
  let { data } = $props()
function update(container) {
  seletectedContainer.set(container)
}
</script>

<section class="w-[80%] m-auto mt-[20px]">
  <div class="flex justify-between">
  <b><h1 class="text-[1.5rem] m-[15px]">Containers</h1></b>
  <a href="/containers/create"><Button content="Create Contianer"/></a>
  </div>
  <div class="flex flex-wrap">
  {#each data.containers as container}
  <ContainerCard img={pihole} name={container.name} status={container.info.status} onClick={() => update(container)}/>
  {/each}
  </div>
</section>
