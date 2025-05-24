<script lang="ts">
  import Button from "$lib/components/Button.svelte"
  import {goto} from "$app/navigation"
  let loading = false;
  
async function createContainer(e: SubmitEvent) {
  loading = true;
  const form = e.currentTarget as HTMLFormElement
  const formData = new FormData(form)


  const name = formData.get("name")
  const image = formData.get("image")
  const data = {"name": name, "image": image};


  await fetch("/api/containers/create", 
    {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    }  
  )

  goto("/containers")
}
</script>

<section class="w-[80%] m-auto mt-[20px]">
 <b><h1 class="text-[1.5rem] m-[15px]">Create Container</h1></b>
  <form on:submit|preventDefault={createContainer} class="w-[100%] border border-[#272727] p-[15px]" action="http://localhost:8000/containers">
  <div class="flex items-center justify-evenly">
  <label class="text-nowrap" for="name">Container Name:</label>
  <input id="name" name="name" class="w-[100%] bg-[#272727] m-[15px]" type='text' placeholder="e.g. Nextjs App"><br>
  </div>
  <div class="flex items-center">
  <label for="image">Image: </label>
  <input class="w-[100%] bg-[#272727] m-[15px]" id="image" name="image" type='text' placeholder="e.g. my-image:my-tag"><br>
  </div>
  {#if loading}
    <Button loading={loading} content="..."/>
  {:else}
    <Button loading={loading}  content="Create Container"/>
  {/if}
  </form>
  </section>

