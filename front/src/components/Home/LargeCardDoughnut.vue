<script setup lang="ts">
import { computed, ref } from 'vue'
import { Chart, DoughnutController, ArcElement, Tooltip } from 'chart.js';
import { DoughnutChart } from 'vue-chart-3';
import axios from 'axios';


Chart.register(DoughnutController, ArcElement, Tooltip);
const baseurl = import.meta.env.VITE_BACK
const labels = ref<string[]>(['1'])
const doughnutRef = ref();
const data = ref<number[]>([1])
const options = ref({
  responsive: true,
  plugins: {

  },
});
const config = {
  Authorization: `JWT ${localStorage.getItem('jwt')}`
}

const get_data = () => {
  axios({
    method: 'GET',
    url: baseurl + 'deliveries/chart/data/',
    headers: config,
  })
    .then((res) => {

      labels.value = res.data.labels
      data.value = res.data.data
    })
}
get_data()
const ChartData = computed(() => ({
  labels: labels.value,
  datasets: [
    {
      data: data.value,
      backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED'],
    },
  ],
}))
</script>

<template>
  <div>
    <el-card class="w-100 ts-all mb-1">
      <DoughnutChart ref="doughnutRef" :chartData="ChartData" :options="options" />
    </el-card>
  </div>
</template>


<style scoped>
.mb-1 {
  margin-bottom: 1rem;
}
</style>