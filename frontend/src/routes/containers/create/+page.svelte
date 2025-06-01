<script lang="ts">
	import { enhance } from '$app/forms';
  import Button from "$lib/components/Button.svelte"
  let loading = false;
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
  <label for="image">Image: </label>
  <input class="w-[100%] bg-[#272727] m-[15px]" id="image" name="image" type='text' placeholder="e.g. my-image:my-tag"><br>
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

