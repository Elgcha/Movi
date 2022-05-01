<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios';
import { useShow } from '../../store/modules/show';
const props = defineProps({
  showDrawer: Boolean,
})
const emit = defineEmits(['locationChange'])
const baseurl = import.meta.env.VITE_BACK
const sido_list = ref<string[]>([''])
const sigungu_list = ref<string[]>([''])
const dong_list = ref<string[]>([''])
const show = useShow()

const config = {
  Authorization: `JWT ${localStorage.getItem('jwt')}`
}
if (sido_list.value[0] === '') {
  axios({
    method: 'GET',
    url: baseurl + 'deliveries/address/',
    headers: config,
  })
    .then((res) => {
      sido_list.value = res.data.sido
    })
}

const sido_change = () => {
  if (!show.sido) { return }
  axios({
    method: 'GET',
    url: baseurl + 'deliveries/address/',
    headers: config,
    params: { sido: show.sido },
  })
    .then((res) => {
      sigungu_list.value = res.data.sigungu
    })
}

const sigungu_change = () => {
  if (!show.sido) { return }
  if (!show.sigungu) { return }
  axios({
    method: 'GET',
    url: baseurl + 'deliveries/address/',
    headers: config,
    params: { sido: show.sido, sigungu: show.sigungu, },
  })
    .then((res) => {
      dong_list.value = res.data.dong
    })
}

// 초기화
const initial = () => {
  show.sido = ''
  show.sigungu = ''
  show.dong = ''
  sigungu_list.value = ['']
  dong_list.value = ['']
}

//확인버튼
const location_change = () => {
  emit("locationChange")
}
</script>


<template>
  <el-drawer
    v-model="props.showDrawer"
    :direction="'rtl'"
    title="지역 선택"
    :size="350"
    :with-header="true"
  >
    <div>시 / 도</div>
    <el-select
      v-model="show.sido"
      class="m-1"
      placeholder="시 / 도"
      size="large"
      @change="sido_change"
    >
      <el-option v-for="item in sido_list" :key="item" :label="item" :value="item" />
    </el-select>
    <div>시 / 군 / 구</div>
    <el-select
      v-model="show.sigungu"
      class="m-1"
      placeholder="시 / 군 / 구"
      size="large"
      @change="sigungu_change"
    >
      <el-option v-for="item in sigungu_list" :key="item" :label="item" :value="item" />
    </el-select>
    <div>동 / 읍 / 면 / 리 / 도로</div>
    <el-select v-model="show.dong" class="m-1" placeholder="읍 / 면 / 리 / 도로" size="large">
      <el-option v-for="item in dong_list" :key="item" :label="item" :value="item" />
    </el-select>
    <template #footer>
      <div style="flex: auto">
        <el-button type="warning" @click="initial">초기화</el-button>
        <el-button type="primary" @click="location_change">확인</el-button>
      </div>
    </template>
  </el-drawer>
</template>


<style scoped>
</style>