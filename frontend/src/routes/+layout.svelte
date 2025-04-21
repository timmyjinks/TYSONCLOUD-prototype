<script>
	import '../app.css';
  import docker from "$lib/assests/docker.png"
  import home from "$lib/assests/home-light.png"
  import {page} from "$app/state"
	let { children } = $props();
</script>

<nav>
	<div class="flex justify-between items-center">
	  <div class="p-[15px] text-[1.5rem]">
        <h1 class="text-[24px]"><b>TYSONCLOUD-prototype</b></h1>
		  </div>
		  <div class="mr-[24px]">
        <div class="flex items-center text-[1.5rem]">
          <a href="/">
          <div class="flex items-center rounded-lg background pt-[5px] pb-[5px] pl-[16px]" aria-current={page.url.pathname === "/"}>
            <img class="color-white" src={home} alt="Home icon" width="32px" height="32px"/>
			      <p class="ml-[16px] pr-[90px] text-[16px]" >Home</p>
          </div>
          </a>
          <a href="/containers" >
          <div class="flex items-center rounded-lg background pt-[5px] pb-[5px] pl-[16px]" aria-current={page.url.pathname === "/containers"}>
            <img src={docker} alt="Docker logo" width="32px" height="32px"/>
			      <p class="ml-[16px] pr-[48px] text-[16px]" >Containers</p>
        </div>
        </a>
		</div>
	</div>
</nav>


<style>
  .background[aria-current=true] {
    background-color: #272727
  }
</style>
{@render children()}
