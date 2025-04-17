<script>
	import '../app.css';
  import docker from "$lib/assests/docker.png"
  import home from "$lib/assests/home.png"
	let { children } = $props();
</script>

<nav>
	<div class="flex justify-between items-center">
	  <div class="p-[15px] text-[1.5rem]">
        <h1 class="text-[24px]"><b>TYSONCLOUD-prototype</b></h1>
		  </div>
		  <div>
        <div class="flex p-[15px] text-[1.5rem]">
          <div class="flex">
            <img src={home} alt="Home icon" width="24px" height="24px"/>
			      <a class="text-[16px]" href="/">Home</a>
          </div>
          <div class="flex ml-[15px]">
            <img src={docker} alt="Docker logo" width="24px" height="24px"/>
			      <a class="text-[16px]" href="/containers">Containers</a>
        </div>
      <!-- </div> -->
		</div>
	</div>
</nav>

{@render children()}
