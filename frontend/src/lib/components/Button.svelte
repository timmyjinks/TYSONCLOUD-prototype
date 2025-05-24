<script lang="ts">
  let {content, loading} = $props()
</script>

<button class="bg-[#ed2939] text-black pr-[15px] pl-[15px] pt-[5px] pb-[5px] m-[15px] rounded-md" disabled={loading} type="submit">{content}</button>
