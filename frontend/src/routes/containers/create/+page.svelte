<script lang="ts">
	import { enhance } from '$app/forms';
  import {Switch } from "$lib/components/ui/switch"
  import Button from "$lib/components/Button.svelte"
  let loading = false;
  let enable_github = false;
  export let form;


  $: if(form?.error) {
    loading = false;
  }
</script>

<section class="w-[80%] m-auto mt-[20px]">
 <b><h1 class="text-[1.5rem] m-[15px]">Create Container</h1></b>
  <form class="w-[100%] border border-[#272727] p-[15px]" action="?/create" method="POST"
        use:enhance={() => {
          loading = true;
        }}>
  <div class="flex items-center justify-evenly">
  <label class="text-nowrap" for="name">Container Name:</label>
  <input id="name" name="name" class="w-[100%] bg-[#272727] m-[15px]" type='text' placeholder="e.g. Nextjs App"><br>
  </div>
  <div class="flex items-center">
  {#if enable_github}

  <label for="github">Github: </label>
  <input class="w-[100%] bg-[#272727] m-[15px]" id="github" name="github" type='text' placeholder="e.g. https://github.com/timmyjinks/TYSONCLOUD-prototype"><br>
  {:else}
  <label for="image">Image: </label>
  <input class="w-[100%] bg-[#272727] m-[15px]" id="image" name="image" type='text' placeholder="e.g. my-image:my-tag"><br>
  {/if}
  </div>
  <div>
    <label for="update-image">Use Github</label>
    <Switch bind:checked={enable_github} id="enable_github" class="m-[15px]"/>
    <input type="hidden" name="enable_github" value={enable_github ? 'true' : 'false' } hidden/>
  </div>
  {#if form?.error}
    <p>{form.error}</p>
  {/if}
  {#if loading}
    <Button loading={true} content="..."/>
  {:else}
    <Button loading={false}  content="Create Container"/>
  {/if}
  </form>
  </section>

