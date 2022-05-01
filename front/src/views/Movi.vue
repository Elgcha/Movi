<script setup lang="ts">
import { onBeforeMount, ref } from 'vue'
import { User, Lock, Message, Expand } from '@element-plus/icons-vue'
import axios from 'axios';


interface rob {
  name: string,
  state: string,
  battery: number,
}

const baseurl = import.meta.env.VITE_BACK
const config = {
  Authorization: `JWT ${localStorage.getItem('jwt')}`
}

const datas = ref<rob[]>()
const get_data = () => {
  axios({
    method: 'GET',
    url: baseurl + 'robots/',
    headers: config,
  })
    .then((res) => {
      datas.value = res.data
    })
}
get_data()

// robot control - not use
const robot_start = () => {
  axios({
    method: 'GET',
    url: baseurl + 'robots/start/',
    headers: config,
  })
    .then((res) => {
      get_data()
    })
}
const robot_end = () => {
  axios({
    method: 'GET',
    url: baseurl + 'robots/end/',
    headers: config,
  })
    .then((res) => {
      get_data()
    })
}

// progress bar
const customColors = [
  { color: '#f56c6c', percentage: 20 },
  { color: '#e6a23c', percentage: 40 },
  { color: '#5cb87a', percentage: 60 },
  { color: '#1989fa', percentage: 80 },
  { color: '#8590e8', percentage: 100 },
]
</script>
<template>
  <el-row>
    <el-col :span="18" :offset="3">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="12" :lg="6" class="mt-1" v-for="data in datas">
          <el-card>
            <h2>{{ data.name }}</h2>
            <h3>상태: {{ data.state }}</h3>
            <el-progress :percentage="data.battery" :color="customColors" />
            <!-- <el-button class="mt-1" @click="robot_start">시작</el-button> 
            <el-button class="mt-1" @click="robot_end">종료</el-button>-->
          </el-card>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>


<style scoped>
.mt-1 {
  margin-top: 1rem;
  color: #8590e8;
}
</style>
