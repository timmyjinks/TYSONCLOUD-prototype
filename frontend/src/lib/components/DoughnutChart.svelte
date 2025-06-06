<script lang="ts">
  import {onMount} from "svelte";
  import Chart from "chart.js/auto"; 

  let status;
  let {title, running, exited, containers} = $props();

const data = {
  labels: ["Running", "Exited"],
  datasets: [
    {
      label: 'Containers',
      data: [exited, running],
      backgroundColor: ["red", "green"],
      borderWidth: 0,
    }
  ]
  };

const config = {
            type: 'doughnut',
            data: data,
          
            options: {
              responsive: true,
              plugins: {
                legend: {
                    position: 'none',
                },
              }
            }
        };
      onMount(()=> {
        const ctx = status.getContext('2d');
        // Initialize chart using default config set
        var myChart = new Chart(ctx, config);
      })
</script>
<div>
  <h3>{title}</h3>
<div class="chart-card">
<div class="flex">
  <div>
    <canvas bind:this={status}></canvas>
  </div>
  <div class="flex justify-center flex-col m-[15px]">
  <p>Running: {running}</p>
  <p class="mb-[5px]">{Math.round(running/containers * 100)}%</p>
  <p>Exited: {exited}</p>
  <p>{Math.round(exited/containers * 100)}%</p>
  </div>
  </div>
</div>
  </div>

<style>
/* Dark mode themed card for Chart.js */
.chart-card {
  background-color: #272727;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  max-width: 600px;
  border: 1px solid #2c3138;
  margin-top: 15px;
}

  </style>
