<script setup lang="ts">
import Navbar from "./components/Navbar/Navbar.vue";
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
</script>

<template>
  <Navbar></Navbar>
  <router-view />
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Dongle:wght@700&family=Nanum+Myeongjo&display=swap");
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  /* font-family: "Nanum Myeongjo", serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

body {
  margin: 0;
}

.m-1 {
  margin: 1rem;
}
.mx-1 {
  margin-left: 1rem;
  margin-right: 1rem;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.my-auto {
  margin-top: auto;
  margin-bottom: auto;
}

.my-1 {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.h-100 {
  height: 100%;
}

.w-100 {
  width: 100%;
}

.justify-content-center {
  justify-content: center;
}

.text-align-center {
  text-align: center;
}

.my-btn {
  justify-content: center;
  align-items: center;
  text-align: center;
  white-space: nowrap;
  cursor: pointer;
  vertical-align: middle;
  border: 1px solid black;
  border-radius: 5px;
}

.my-btn:hover {
  border: 1px solid blue;
}
.ts-all {
  transition: all ease 0.5s;
}
.cursor-pointer {
  cursor: pointer;
}
.position-relative {
  position: relative;
}

/* th {
  cursor: pointer;
  transition: all;
}

th:hover {
  transform: scale(1.02);
} */
</style>
