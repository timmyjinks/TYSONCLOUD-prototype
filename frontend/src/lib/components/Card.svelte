<script lang="ts">
  let {amount, img, title} = $props();
</script>

<div class="flex w-[600px] bg-[#272727] justify-between items-center rounded-lg m-[15px]">
  <div class="flex items-center ">
    <div class="p-[15px]">
      <img src={img} alt="skibidi" width="40px" height="40px" />
    </div>
    <div>
      <h2>{title}</h2>
    </div>
  </div>
  <div class="flex border-l p-[20px]">
    <h1 class="text-[1.5rem]">{amount}</h1>
  </div>
</div>
