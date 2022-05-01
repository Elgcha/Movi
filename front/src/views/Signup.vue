<script setup lang="ts">
import { ref } from 'vue';
import { User, Lock, Message } from '@element-plus/icons-vue';
import axios from 'axios';
import { useRouter, useRoute } from 'vue-router'
// import router from '../router';

const baseurl = import.meta.env.VITE_BACK
const router = useRouter()
const route = useRoute()
const userdata = ref({ 'username': '', 'email': '', 'password': '', 'passwordConfirm': '' })
const error = ref({ 'username': '', 'email': '', 'password': '', 'passwordConfirm': '' })
const show_alert = ref<boolean>(false);
const isLoading = ref<boolean>(false)
const off_alert = () => {
  show_alert.value = false
}
const check: () => boolean = () => {
  let result: boolean = true
  if (!userdata.value.username) {
    error.value.username = '닉네임은 필수입니다.'
    result = false
  } else {
    error.value.username = ''
  }
  if (!userdata.value.email) {
    error.value.email = '이메일은 필수입니다.'
    result = false
  } else {
    error.value.email = ''
  }
  if (!userdata.value.password) {
    error.value.password = '비밀번호는 필수입니다.'
    result = false
  } else {
    error.value.password = ''
  }
  if (userdata.value.passwordConfirm !== userdata.value.password) {
    error.value.passwordConfirm = '비밀번호와 동일해야합니다.'
    result = false
  } else {
    error.value.passwordConfirm = ''
  }

  return result;
}

const signupRequest = (e: Event) => {
  e.preventDefault();
  if (!check()) { return }
  isLoading.value = true
  axios({
    method: 'POST',
    url: baseurl + 'accounts/signup/',
    data: userdata.value
  })
    .then((res) => {
      router.push({ name: "Login" })
    })
    .catch((err) => {
      show_alert.value = true
      setTimeout(() => {
        show_alert.value = false
      }, 5000);
    })
}
</script>


<template>
  <el-alert
    title="회원가입 실패"
    type="warning"
    class="alert"
    v-show="show_alert"
    description="이미 존재하는 닉네임입니다."
    show-icon
    @close="off_alert"
  />
  <el-container class="signup justify-content-center">
    <el-card class="mx-auto mt-40 w-signup">
      <h2 class="mb-40">Signup</h2>
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
          <el-input v-model="userdata.email" placeholder="Email" :prefix-icon="Message"></el-input>
          <div class="error">{{ error.email }}</div>
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
          <el-input
            v-model="userdata.passwordConfirm"
            placeholder="Password Confirm"
            type="password"
            :prefix-icon="Lock"
          ></el-input>
          <div class="error">{{ error.passwordConfirm }}</div>
        </el-form-item>
        <el-form-item>
          <el-button
            @click="signupRequest"
            class="w-100 mt-40"
            type="primary"
            native-type="submit"
            block
          >Signup</el-button>
          <div class="des">가입 요청 승인 후, 이용 가능합니다.</div>
        </el-form-item>
      </el-form>
    </el-card>
  </el-container>
</template>


<style scoped>
.des {
  font-size: 0.8rem;
  color: grey;
  padding: 3px;
}
.signup {
  text-align: center;
}
.bg-signup {
  background-color: rgb(168, 168, 168);
}

.mt-40 {
  margin-top: 40px;
}

.mb-40 {
  margin-bottom: 40px;
}

.w-signup {
  width: 30%;
}
</style>