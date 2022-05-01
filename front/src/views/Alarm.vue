<script setup lang="ts">
import { ref } from 'vue'
import { User, Lock, Message, Expand } from '@element-plus/icons-vue'
import axios from 'axios';
import type { ElTable } from 'element-plus'

interface alarm {
  id: number
  content: string
  user: string
  title: string
  check: boolean
}
const tableData = ref<alarm[]>()
const baseurl = import.meta.env.VITE_BACK
const config = {
  Authorization: `JWT ${localStorage.getItem('jwt')}`
}
const get_data = () => {
  axios({
    method: 'GET',
    url: baseurl + 'deliveries/alarm/',
    headers: config,
    // params: { page: show.page },
  })
    .then((res) => {
      if (res.data) {
        tableData.value = res.data.reverse()
      } else {
        tableData.value = []
      }
      // page_data.value = res.data.page
    })
    .catch((err) => {
      // console.log(err)
      // localStorage.removeItem('jwt')
      // router.push('/login')
    })
}
get_data()


const multipleTableRef = ref<InstanceType<typeof ElTable>>()
const multipleSelection = ref<alarm[]>([])
const toggleSelection = (rows?: alarm[]) => {
  if (rows) {

  }
}

const select_delete = () => {
  const temp_data: number[] = []
  multipleSelection.value.map((now) => {
    temp_data.push(now.id)
  })
  axios({
    method: 'DELETE',
    url: baseurl + 'deliveries/alarm/delete/',
    headers: config,
    data: temp_data
  })
    .then((res) => {
      get_data()
    })
    .catch((err) => {
      // console.log(err)
    })
}

const createAlarm = () => {
  const data = {
    'user': 'test',
    'check': false,
    'title': 'test',
    'content': 'asd',
    'type': 'test',
  }
  axios({
    method: 'POST',
    url: baseurl + 'deliveries/alarm/create/',
    headers: config,
    data: data,
  })
    .then((res) => {
      get_data()
    })
    .catch((err) => {
      // console.log(err)
    })
}


const handleSelectionChange = (val: alarm[]) => {
  multipleSelection.value = val
}


const activeUser = (id: number, content: string) => {
  let arr = content.split(' ')
  let username = arr[10]
  let data = {
    'username': username,
    'id': id
  }
  axios({
    method: 'POST',
    url: baseurl + 'accounts/active/',
    headers: config,
    data: data
  })
    .then((res) => {
      tableData.value = tableData.value?.filter((data) => {
        if (data.id === id) {
          return false
        } else {
          return true
        }
      })
    })
    .catch((err) => {
      // console.log(err)
    })
}

const reject = (id: number) => {
  let data = [id]
  axios({
    method: 'DELETE',
    url: baseurl + 'deliveries/alarm/delete/',
    headers: config,
    data: data
  })
    .then((res) => {
      get_data()
    })
}
</script>
<template>
  <div>
    <el-row justify="center" class="mt-2">
      <el-col :span="3"></el-col>
      <el-col :span="18">
        <el-table
          @selection-change="handleSelectionChange"
          ref="multipleTableRef"
          :data="tableData"
          class="m-1"
          stripe
          style="width: 100%"
        >
          <el-table-column type="selection" />
          <el-table-column prop="id" label="ID" />
          <el-table-column prop="title" label="Title" />
          <el-table-column type="expand">
            <template #default="props">
              <p class="test">{{ props.row.content }}</p>
              <el-button
                v-if="props.row.type === 'new'"
                class="m-1"
                @click="activeUser(props.row.id, props.row.content)"
                type="success"
              >승인</el-button>
              <el-button
                v-if="props.row.type === 'new'"
                @click="reject(props.row.id)"
                class="m-1"
                type="warning"
              >거절</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-button @click="select_delete">선택한 알림 삭제</el-button>
        <!-- <el-button @click="createAlarm">전체 삭제</el-button> -->
      </el-col>
      <el-col :span="3"></el-col>
    </el-row>
  </div>
</template>


<style scoped>
.test {
  white-space: pre-line;
  padding: 1rem 2rem;
}
</style>
