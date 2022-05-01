<script setup lang="ts">
import { ref } from 'vue'
import { User, Lock, Message } from '@element-plus/icons-vue'
import axios from 'axios';
import { useRouter, useRoute } from 'vue-router'
import { useUser } from '../store/modules/user'

const baseurl = import.meta.env.VITE_BACK
const userdata = ref({ 'username': '', 'password': '' })
const error = ref({ 'username': '', 'password': '' })
const show_alert = ref<boolean>(false);
const isLoading = ref<boolean>(false)
const router = useRouter()
const route = useRoute()
const user = useUser()

const off_alert = () => {
  show_alert.value = false
}
const check: () => boolean = () => {
  let result: boolean = true
  if (!userdata.value.username) {
    error.value.username = '아이디를 입력해주세요.'
    result = false
  } else {
    error.value.username = ''
  }
  if (!userdata.value.password) {
    error.value.password = '비밀번호를 입력해주세요.'
    result = false
  } else {
    error.value.password = ''
  }

  return result;
}

const loginRequest = (e: Event) => {
  e.preventDefault();
  if (!check()) { return }
  isLoading.value = true
  axios({
    method: 'POST',
    url: baseurl + 'accounts/api-token-auth/',
    data: userdata.value
  })
    .then((res) => {
      user.setUsername(userdata.value.username)
      localStorage.setItem('jwt', res.data.token)
      router.push({ name: "Home" })
      // console.log(res.data.token)
    })
    .catch((err) => {
      show_alert.value = true
    })
}

</script>


<template>
  <el-alert
    title="로그인 실패"
    type="warning"
    class="alert"
    v-show="show_alert"
    description="로그인에 실패하였습니다. 아이디와 비밀번호를 확인해주세요. 또는, 가입 승인을 기다려주세요."
    show-icon
    @close="off_alert"
  />
  <el-container class="login justify-content-center">
    <el-card class="mx-auto mt-40 w-login">
      <h2 class="mb-40">Login</h2>
      <el-form class="w-100" ref="form">
        <el-form-item>
          <el-input
            v-model="userdata.username"
            maxlength="12"
            placeholder="Username"
            :prefix-icon="User"
          ></el-input>
          <div class="error">{{ error.username }}</div>
        </el-form-item>
        <el-form-item>
          <el-input
            v-model="userdata.password"
            placeholder="Password"
            type="password"
            :prefix-icon="Lock"
          ></el-input>
          <div class="error">{{ error.password }}</div>
        </el-form-item>
        <el-form-item>
          <el-button
            @click="loginRequest"
            class="w-100 mt-40"
            type="primary"
            native-type="submit"
            block
          >Login</el-button>
        </el-form-item>
        <router-link to="/signup" class="signup">
          <el-button class="w-100" type="warning" native-type="submit" block>Signup</el-button>
        </router-link>
      </el-form>
    </el-card>
  </el-container>
</template>


<style scoped>
.login {
  text-align: center;
}
.bg-login {
  background-color: rgb(168, 168, 168);
}

.mt-40 {
  margin-top: 40px;
}

.mb-40 {
  margin-bottom: 40px;
}

.w-login {
  width: 30%;
}
.error {
  color: rgb(206, 164, 101);
}
.alert {
  position: absolute;
}
@media (max-width: 720px) {
  .w-login {
    width: 100%;
  }
}
@media (max-width: 1080px) {
  .w-login {
    width: 60%;
  }
}
@media (max-width: 1200px) {
  .w-login {
    width: 50%;
  }
}

.signup {
  text-decoration: none;
  color: black;
  text-align: end;
}
.signup:hover {
  color: gray;
}
</style>