<script setup lang="ts">
import { onBeforeMount, ref, watch } from "vue";
import { Avatar, BellFilled, Close, Menu, WarningFilled, Bell } from '@element-plus/icons-vue'
import { useRouter, useRoute } from 'vue-router'
import { useUser } from '../../store/modules/user'
import axios from "axios";


const menu = ref(false);
const user = useUser();
const baseurl = import.meta.env.VITE_BACK
const config = {
  Authorization: `JWT ${localStorage.getItem('jwt')}`
}
const show_alert = ref(false);
const offMenu = () => {
  menu.value = false;
}
const off_alert = () => {
  show_alert.value = false
}
const router = useRouter()
const route = useRoute()
const controlMenu = () => {
  menu.value = !menu.value;
}
const LogoutRequest = () => {
  localStorage.removeItem('jwt')
  menu.value = false;
  router.push({ name: 'Login' })
}
const jwt_check = () => {
  axios({
    method: 'POST',
    url: baseurl + 'accounts/api/token/verify/',
    data: { 'token': localStorage.getItem('jwt') }
  })
    .then((res) => {
    })
    .catch((err) => {
      localStorage.removeItem('jwt')
      router.push('/login')
    })
}
jwt_check()
const login_check = watch(route, () => {

  if (!localStorage.getItem('jwt')) {
    if (route.name === 'Signup') { }
    else if (route.name === 'Login') { }
    else { router.push('/login'); show_alert.value = true; setTimeout(() => { show_alert.value = false }, 3000) }
    // router.push('/login')
  } else {
    alarmCheck()
    if (route.name === 'Signup') {
      router.push('/')
    } else if (route.name === 'Login') {
      router.push('/')
    }
  }
}


)
const alarmCheck = () => {
  axios({
    method: 'GET',
    url: baseurl + 'deliveries/alarm/check/',
    headers: config,
    // params: { page: show.page },
  })
    .then((res) => {
      user.newAlarm = res.data
    })
}
alarmCheck()
const moveToAlarm = () => {
  router.push('/alarm')
}

const moveToHome = () => {
  router.push('/')
}



</script>

<template>
  <el-alert
    class="alert"
    v-show="show_alert"
    title="로그인이 필요합니다"
    type="warning"
    show-icon
    @close="off_alert"
  />
  <el-drawer
    v-model="menu"
    :direction="'ltr'"
    :title="user.username"
    :size="350"
    :with-header="true"
  >
    <router-link to="/" class="drawer-item" @click="offMenu">Home</router-link>
    <router-link to="/detail" class="drawer-item" @click="offMenu">Detail</router-link>
    <router-link to="/movi" v-show="user.staff" class="drawer-item" @click="offMenu">Movi</router-link>
    <div class="cursor-pointer mt-3" @click="LogoutRequest">Logout</div>
  </el-drawer>
  <el-row id="nav" class="bg-nav align-itmes-center">
    <el-col :span="3" :xs="3" :sm="3" :lg="3">
      <!-- <img @click="moveToHome" class="m-1 cursor-pointer" src="/Movi-logo.png" width="60" /> -->
      <div @click="moveToHome" class="logo">Movi</div>
    </el-col>
    <el-col
      :span="1"
      :offset="19"
      :xs="{ span: 1, offset: 17 }"
      :sm="{ span: 1, offset: 18 }"
      :lg="{ span: 1, offset: 19 }"
    >
      <BellFilled @click="moveToAlarm" class="icon" :class="{ 'color-alarm': user.newAlarm }" />
      <!-- <Bell v-else @click="moveToAlarm" class="icon" /> -->
    </el-col>
    <el-col
      :span="1"
      :offset="1"
      :xs="{ span: 1, offset: 1 }"
      :sm="{ span: 1, offset: 0 }"
      :lg="{ span: 1, offset: 0 }"
      class="my-auto"
      @click="controlMenu"
    >
      <Menu class="icon" />
    </el-col>
  </el-row>
</template>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Dongle:wght@700&display=swap");
.drawer-item {
  margin-bottom: 1rem;
  display: block;
  text-decoration: none;
  color: Black;
}
.logo {
  color: white;
  /* padding: 1px; */
  font-family: "Dongle", sans-serif;
  font-size: 3rem;
  margin: -2px 0 -2px 1rem;
  cursor: pointer;
}

.router-link-exact-active {
  color: blue;
}
.align-itmes-center {
  align-items: center;
}
.bg-nav {
  background-color: rgb(191, 209, 216);
}

.vertical-align-center {
  vertical-align: center;
}
.icon {
  height: 2rem;
  display: inline;
  cursor: pointer;
}

.alert {
  position: absolute;
  top: 3rem;
  z-index: 10;
}

.color-alarm {
  color: rgb(222, 84, 68);
}
.mt-3 {
  margin-top: 3rem;
}
</style>