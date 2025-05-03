<script lang="ts">
  import {page} from "$app/state"
  import {goto} from "$app/navigation"
  import Button from "$lib/components/Button.svelte"
  import {seletectedContainer} from "$lib/store"
  import deletes from "$lib/assests/delete.png"
  const name = page.url.pathname.split("/")[2]
  console.log($seletectedContainer)

async function updateContainer(e: SubmitEvent) {
  e.preventDefault()
  const form = e.currentTarget as HTMLFormElement;
  const formData = new FormData(form);

  const new_name = formData.get("new_name")
  const image = formData.get("image")
  const data = {"id": $seletectedContainer.id, "new_name": new_name, "image": image};

  await fetch(`/api/container/${name}`, 
    {
      method: "PUT",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    }
  )
  goto("/containers")
}


async function deleteContainer() {
  await fetch(`/api/container/${name}`,
    {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({"id": $seletectedContainer.id})
    }
  )
  goto("/containers")
}


</script>
<section class="w-[80%] m-auto mt-[20px]">
  <div class="flex items-center justify-between">
 <b><h1 class="text-[1.5rem] m-[15px]">{name}</h1></b>
  <button onclick={deleteContainer}><img src={deletes} alt="cook" width="24px" height="24px" class="text-right"/></button>
  </div>
  <form onsubmit={updateContainer} class="border p-[15px]"  method="post">
  <div class="flex items-center">
  <label class="text-nowrap" for="new_name">Container Name: </label>
  <input name="new_name" class="bg-[#272727] w-[100%] m-[15px]" type='text' placeholder="e.g. Nextjs App"><br>
  </div>
  <div class="flex items-center">
  <label class="text-nowrap" for="image">Image: </label>
  <input class="bg-[#272727] w-[100%] m-[15px]" name="image" type='text' placeholder="e.g. my-image:my-tag"><br>
  </div>
  <Button content="Update Container"/>
  </form>
  </section>

