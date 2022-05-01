<script setup lang="ts">
import { onBeforeMount, ref } from 'vue'
import { User, Lock, Message, Expand, Search, Plus, Refresh } from '@element-plus/icons-vue'
import axios from 'axios';
import router from '../router';
import Fuse from 'fuse.js'
import { useShow } from '../store/modules/show'
import CreateData from '../components/Detail/CreateData.vue'
import { useUser } from '../store/modules/user';

interface data_user {
  username: string
  email: string | null
}

interface data_address {
  id: number
  sido: string // 서울시
  sigungu: string  // 강남구
  dong: string  // 테헤란로
  doro: string  // 245
}

interface data_category {
  id: number
  name: string
}
interface box {
  id: number
  number: number
  state: string
  user: data_user
  address: data_address
  category: data_category

}

const baseurl = import.meta.env.VITE_BACK
const config = {
  Authorization: `JWT ${localStorage.getItem('jwt')}`
}
const show = useShow()
const user = useUser();
const search_keyword = ref<string>('')
let viewWidth = ref(window.innerWidth)
const data = ref<box[]>([])
const origin_data = ref<box[]>([])
const view_data = ref<box[]>([])
const page_data = ref({ countAll: 0, current: 1, pageSize: 10, searched: false })
const page_change = (page: number) => {
  const s = (page - 1) * page_data.value.pageSize
  view_data.value = data.value.slice(s, s + page_data.value.pageSize)
  page_data.value.current = page
}

const get_data = () => {
  axios({
    method: 'GET',
    url: baseurl + 'deliveries/detail/',
    headers: config,
    // params: { page: show.page },
  })
    .then((res) => {
      // console.log(res.data)
      data.value = res.data
      origin_data.value = res.data
      page_change(page_data.value.current)
      page_data.value.countAll = res.data.length
      // page_data.value = res.data.page
    })
    .catch((err) => {
      // console.log(err)
      // localStorage.removeItem('jwt')
      // router.push('/login')
    })
}
get_data()

const search = () => {
  const options = {
    includeScore: false,
    keys: ['id', 'user.username', 'state', 'address.sido', 'address.sigungu', 'address.dong', 'category.name', '  etc']
  }

  const fuse = new Fuse(data.value, options)

  const result = fuse.search(search_keyword.value)
  const view_result = result.map((item) => {
    return item.item
  })
  data.value = view_result
  view_data.value = view_result.slice(0, page_data.value.pageSize)
  page_data.value.countAll = view_result.length
  page_data.value.current = 1
  page_data.value.searched = true
}

const Data_add = () => {
  show.add = !show.add
}

const initial = () => {
  data.value = origin_data.value
  page_change(1)
  page_data.value.searched = false
  search_keyword.value = ''
}
</script>


<template>
  <CreateData v-show="show.add"></CreateData>
  <el-row justify="center" class="mt-2">
    <el-col :span="3"></el-col>
    <el-col :span="18" class="relative">
      <el-input
        class="w-input m-1"
        clearable
        v-model="search_keyword"
        @keyup.enter="search"
        :prefix-icon="Search"
      />
      <el-button
        @click="initial"
        class="initial-btn"
        v-show="page_data.searched"
        type="primary"
        plain
      >초기화</el-button>
      <el-button class="ml-btn" type="primary" @click="get_data" plain>
        <Refresh class="icon"></Refresh>
      </el-button>
      <!-- <el-button type="primary" v-show="user.staff" @click="Data_add" plain>
        <Plus class="icon"></Plus>
      </el-button>-->
      <el-table :data="view_data" stripe style="width: 100%">
        <el-table-column prop="id" label="ID" width="50%" />
        <el-table-column prop="user.username" label="User" width="70%" />
        <el-table-column prop="category.name" label="Category" width="100%" />
        <el-table-column prop="state" label="State" width="70%" />
        <el-table-column label="Address">
          <template
            #default="scope"
          >{{ scope.row.address.sido + ' ' + scope.row.address.sigungu + ' ' + scope.row.address.dong }}</template>
        </el-table-column>
        <el-table-column v-if="viewWidth > 800" prop="etc" label="etc" />
      </el-table>
    </el-col>
    <el-col :span="3"></el-col>
    <el-pagination
      :page-size="page_data.pageSize"
      layout="prev, pager, next"
      :total="page_data.countAll"
      :current-page="page_data.current"
      @current-change="page_change"
    />
  </el-row>
</template>


<style scoped>
.icon {
  height: 1rem;
  display: inline;
  cursor: pointer;
}
.mt-2 {
  margin-top: 2rem;
}
.ml-btn {
  margin-left: 70%;
}
.w-input {
  width: 20%;
}
.relative {
  position: relative;
}
.initial-btn {
  position: absolute;
  display: inline;
  top: 16px;
  margin-left: -6px;
}

@media (max-width: 720px) {
  .w-input {
    width: 70%;
  }
  .ml-btn {
    margin-left: 15%;
  }
}
@media (max-width: 1080px) {
  .w-input {
    width: 60%;
  }
  .ml-btn {
    margin-left: 15%;
  }
}
@media (max-width: 1200px) {
  .w-input {
    width: 40%;
  }
  .ml-btn {
    margin-left: 21%;
  }
}
</style>