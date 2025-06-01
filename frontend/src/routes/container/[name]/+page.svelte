<script lang="ts">
  import {page} from "$app/state"
	import { enhance } from '$app/forms';
  import {Switch} from "$lib/components/ui/switch/index"
  import Button from "$lib/components/Button.svelte"
  import {selectedContainer} from "$lib/store"
  import deletes from "$lib/assests/delete.png"
  const name = page.url.pathname.split("/")[2]
  let loading = false;
  let update_image = false;
  let error = "";
  export let form;

  $: if(form?.error) {
    loading = false;
  }
console.log($selectedContainer)

</script>
<section class="w-[80%] m-auto mt-[20px]">
  <div class="flex items-center justify-between">
 <b><h1 class="text-[1.5rem] m-[15px]">{name}</h1></b>
  <form method="post" action="?/delete">
  <input type="hidden" name="id" value={$selectedContainer?.id}/>
  <button type="submit"><img src={deletes} alt="cook" width="24px" height="24px" class="text-right"/></button>
  </div>
  <form action="?/update" use:enhance={() => {loading = true;}} class="border p-[15px]"  method="post">
  <div class="flex items-center">
  <label class="text-nowrap" for="new_name">Container Name:</label>
  <input name="new_name" class="bg-[#272727] w-[100%] m-[15px]" type='text' placeholder="e.g. Nextjs App"><br>
  <input type="hidden" name="id" value={$selectedContainer?.id}/>
  </div>
  <div class="flex items-center">
  <label class="text-nowrap" for="image">Image: </label>
  <input class="bg-[#272727] w-[100%] m-[15px]" name="image" type='text' placeholder="e.g. my-image:my-tag"><br/>
  </div>
  <div class="flex items-center">
    <label for="update-image">Update container</label>
    <Switch bind:checked={update_image} id="update-image" class="m-[15px]"/>
    <input type="hidden" name="update_image" value={update_image ? 'true' : 'false' } hidden/>
  </div>
  <div class="flex items-center">
    <a class="mt-[15px] hover:text-red-500" href={"https://mangomongo-" + name + ".tysonjenkins.dev"}>{"https://mangomongo-" + name + ".tysonjenkins.dev"}</a>
  </div>
  <br/>
  {#if form?.error}
    <p>{form?.error}</p>
  {/if}
  <p>{error}</p>

  {#if loading}
    <Button loading={loading} content="..."/>
  {:else}
    <Button loading={loading}  content="Update Container"/>
  {/if}
  </form>
  </section>

