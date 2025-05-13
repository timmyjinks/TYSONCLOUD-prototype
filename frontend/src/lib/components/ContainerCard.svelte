<script lang="ts">
  let {img, status, name, onClick} = $props();
</script>

<div class="w-[100%] bg-[#272727] rounded-lg m-[15px]">
<a class="p-[0]" href={`/container/${name}`} onclick={onClick}>
  <div class="flex items-center">
    <div class="p-[15px]">
      <img src={img} alt="skibidi" width="40px" height="40px" />
    </div>
    <div>
      <h2>{name}</h2>
      <p>{status}</p>
    </div>
  </div>
  </a>
</div>
