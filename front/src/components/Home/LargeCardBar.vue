<script setup lang="ts">
import { computed, ref } from 'vue'
import { Chart, BarController, ArcElement, Tooltip, registerables } from 'chart.js';
import { BarChart, PolarAreaChart } from 'vue-chart-3';
import axios from 'axios';


Chart.register(...registerables);
const baseurl = import.meta.env.VITE_BACK
const labels = ref<string[]>(['1', '2', '3', '4'])
const barRef = ref();
const data = ref<number[]>([1, 2, 3, 4])
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
    url: baseurl + 'deliveries/chart/data/2',
    headers: config,
  })
    .then((res) => {
      // console.log(res)
      labels.value = res.data.labels
      data.value = res.data.data
    })
}
get_data()
const ChartData = computed(() => ({
  labels: labels.value,
  datasets: [
    {
      label: '수량(개)',
      data: data.value,
      backgroundColor: ['rgb(220, 121, 121)', 'rgb(219, 223, 152)', '#123E6B', '#97B0C4', '#A5C8ED'],
    },
  ],
}))
</script>

<template>
  <div>
    <el-card class="w-100 ts-all mb-1">
      <BarChart ref="barRef" :chartData="ChartData" :options="options" />
    </el-card>
  </div>
</template>


<style scoped>
.mb-1 {
  margin-bottom: 1rem;
  color: rgb(219, 223, 152);
}
</style>