<script setup lang="ts">
import { onBeforeMount, ref } from 'vue'
import { User, Lock, Message, Expand } from '@element-plus/icons-vue'
import axios from 'axios';
import router from '../router';
import SmallCard from '../components/Home/SmallCard.vue';
import LocationDrawer from '../components/Home/LocationDrawer.vue'
import { useShow } from '../store/modules/show'
import { useUser } from '../store/modules/user';
import LargeCard from '../components/Home/LargeCard.vue';
import LargeCardDoughnut from '../components/Home/LargeCardDoughnut.vue';
import LargeCardBar from '../components/Home/LargeCardBar.vue';



const baseurl = import.meta.env.VITE_BACK
const data = ref({ all: 1, move: 0, wait: 0, complete: 0, })
const show = useShow()
const user = useUser()
const config = {
  Authorization: `JWT ${localStorage.getItem('jwt')}`
}
// 지역 drawer
const location = ref<boolean>(false)
const location_c = () => {
  location.value = !location.value
}
const location_btn = ref<boolean>(false)
const changeLocation = () => {
  location_btn.value = !location_btn.value
  if (location_btn.value) {
    location.value = true
  } else {
    location.value = false
    get_data()
  }
}

const get_user = () => {
  axios({
    method: 'POST',
    url: baseurl + 'accounts/check/',
    headers: config,
  })
    .then((res) => {
      user.username = res.data.username
      user.staff = res.data.staff
    })
}
get_user()

// 기본 데이터 가져오기
const get_data = () => {
  // location.value = false
  if (user.staff === false) {
    axios({
      method: 'GET',
      url: baseurl + 'deliveries/user/main/',
      headers: config,
    })
      .then((res) => {

        data.value = res.data
      })
      .catch(() => {
        // router.push('/login')
      })
    return
  }
  if (show.sido && location.value) {
    axios({
      method: 'GET',
      url: baseurl + 'deliveries/search/location/',
      headers: config,
      params: {
        sido: show.sido,
        sigungu: show.sigungu,
        dong: show.dong,
      }
    })
      .then((res) => {
        // console.log(res.data)
        data.value = res.data
      })
      .catch(() => {
        // router.push('/login')
      })

  } else {

    axios({
      method: 'GET',
      url: baseurl + 'deliveries/',
      headers: config
    })
      .then((res) => {
        data.value = res.data
      })
      .catch(() => {
        // router.push('/login')
      })
  }
}
get_data()




</script>

<template>
  <LocationDrawer @locationChange="get_data" :show-drawer="location"></LocationDrawer>
  <el-row class="text-align-center mt-20">
    <el-col :xs="22" :sm="3" :offset="1">
      <el-row class="mb-1 controllerWrap" :gutter="10">
        <el-col :span="12" :sm="24">
          <el-button
            @click="show.changeAll"
            class="ts-all mt-1 w-100"
            :class="{ 'checked': show.all }"
            plain
          >총 수량</el-button>
        </el-col>
        <el-col :span="12" :sm="24">
          <el-button
            @click="show.changeWait"
            class="ts-all mt-1 w-100"
            :class="{ 'checked': show.wait }"
            plain
          >대기 중</el-button>
        </el-col>
        <el-col class="mt-1" :span="12" :sm="24">
          <el-button
            @click="show.changeMove"
            class="ts-all w-100"
            :class="{ 'checked': show.move }"
            plain
          >배송 중</el-button>
        </el-col>
        <el-col class="mt-1" :span="12" :sm="24">
          <el-button
            @click="show.changeComplete"
            class="ts-all w-100"
            :class="{ 'checked': show.complete }"
            plain
          >완료</el-button>
        </el-col>
        <el-col class="mt-1" :span="12" :sm="24">
          <el-button
            class="w-100"
            @click="show.changegraph1"
            :class="{ 'checked': show.graph1 }"
            plain
          >지역별</el-button>
        </el-col>
        <el-col class="mt-1" :span="12" :sm="24">
          <el-button
            class="w-100"
            @click="show.changegraph2"
            :class="{ 'checked': show.graph2 }"
            plain
          >손실</el-button>
        </el-col>
        <el-col class="mt-1" :span="12" :sm="24" v-if="user.staff">
          <el-button
            plain
            @click="changeLocation"
            class="ts-all w-100"
            :class="{ 'checked': location_btn }"
          >
            <span>지역 검색</span>
            <span>
              <Expand class="icon"></Expand>
            </span>
          </el-button>
        </el-col>
        <el-col class="mt-1" :span="12" :sm="24">
          <el-button class="w-100" @click="get_data" plain>새로고침</el-button>
        </el-col>
      </el-row>
    </el-col>
    <el-col :xs="24" :sm="15" :offset="1">
      <el-row :gutter="10">
        <transition-group name="fade" mode="out-in">
          <el-col :xs="22" :sm="6" v-show="show.all" key="1">
            <SmallCard name="총 수량" :number="data.all" icon="Box"></SmallCard>
          </el-col>
          <el-col :xs="22" :sm="6" v-show="show.wait" key="2">
            <SmallCard name="대기 중" :number="data.wait" icon="Wait"></SmallCard>
          </el-col>
          <el-col :xs="22" :sm="6" v-show="show.move" key="3">
            <SmallCard name="이동 중" :number="data.move" icon="Move"></SmallCard>
          </el-col>
          <el-col :xs="22" :sm="6" v-show="show.complete" key="4">
            <SmallCard name="이동 완료" :number="data.complete" icon="Complete"></SmallCard>
          </el-col>
          <el-col :span="22" :sm="12" v-show="show.graph1" key="5">
            <LargeCardDoughnut></LargeCardDoughnut>
          </el-col>
          <el-col :span="22" :sm="12" v-show="show.graph2" key="6">
            <LargeCardBar></LargeCardBar>
          </el-col>
        </transition-group>
      </el-row>
    </el-col>
    <el-col :span="4"></el-col>
  </el-row>
</template>


<style scoped>
.controllerWrap {
  border: 1px solid rgb(161, 206, 164);
  border-radius: 10px;
  padding: 10px 5px;
}
.fade-item {
  display: inline-block;
  margin-right: 10px;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}
.fade-move {
  transition: transform 0.5s;
}
.fade-item {
  transition: all 0.5s;
  display: inline-block;
  margin-right: 10px;
}
.fade-enter, .fade-leave-to
/* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}
.fade-leave-active {
  position: absolute;
}
.icon {
  height: 1rem;
  margin-left: 2px;
}
.mt-20 {
  margin-top: 20px;
}

.mt-1 {
  margin-top: 1rem;
}
.mb-1 {
  margin-bottom: 1rem;
}
.checked {
  border: none;
  background-color: rgb(142, 179, 214);
  color: white;
}
</style>