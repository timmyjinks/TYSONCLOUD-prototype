<script lang="ts">
  import {page} from "$app/state"
  import Button from "$lib/components/Button.svelte"
</script>


<section class="w-[80%] m-auto mt-[20px]">
 <b><h1 class="text-[1.5rem] m-[15px]">Create Container</h1></b>
  <form class="border p-[15px]" action="">
  <label for="name">Container Name: </label>
  <input id="name" class="border w-[80%] m-[15px]" type='text' placeholder="e.g. Nextjs App"><br>
  <label for="image">Image: </label>
  <input class="border w-[80%] m-[15px]" id="image" type='text' placeholder="e.g. my-image:my-tag"><br>
  <Button content="Create Container"/>
  </form>





  </section>

