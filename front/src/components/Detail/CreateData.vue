<script setup lang="ts">
import axios from 'axios';
import { onBeforeMount, ref } from 'vue'
import { useShow } from '../../store/modules/show'


const show = useShow()
const box_data = ref({ category: '', state: '대기', number: '', user: '', address: '', })

const baseurl = import.meta.env.VITE_BACK
const config = {
  Authorization: `JWT ${localStorage.getItem('jwt')}`
}
const create_data = () => {
  axios({
    method: 'POST',
    url: baseurl + 'deliveries/create/',
    headers: config,
    data: box_data.value
  })
    .then((res) => {
      show.add_check = true;
      setTimeout(() => {
        show.add_check = false;
      }, 2000);
    })
    .catch((err) => {
      // console.log(err)
    })
}

const off_alert = () => {
  show.add_check = false
}
</script>


<template>
  <el-drawer v-model="show.add" :direction="'rtl'" title="추가" :size="350" :with-header="true">
    <el-alert
      class="alert"
      v-show="show.add_check"
      title="정상적으로 추가되었습니다"
      type="success"
      show-icon
      @close="off_alert"
    />
    <div>담당 기사</div>
    <el-input v-model="box_data.user" class="m-1 add_input" />
    <div>카테고리</div>
    <el-input v-model="box_data.category" class="m-1 add_input" />
    <div>번호</div>
    <el-input v-model="box_data.number" class="m-1 add_input" />
    <div>주소</div>
    <el-input v-model="box_data.address" class="m-1 add_input" />
    <template #footer>
      <div style="flex: auto">
        <el-button type="warning">초기화</el-button>
        <el-button @click="create_data" type="primary">추가</el-button>
      </div>
    </template>
  </el-drawer>
</template>


<style scoped>
.alert {
  position: absolute;
  z-index: 10;
  width: 70%;
  top: 3rem;
}
.add_input {
  width: 70%;
}
</style>