<template>
  <div class="e404-container">
    <Warning class="icon"></Warning>
    <h1>404 NOT FOUND</h1>
    <router-link to="/">Home</router-link>
  </div>
</template>

<script setup lang="ts">
import { Warning } from '@element-plus/icons-vue'
</script>

<style scoped>
.e404-container {
  width: 70%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

.icon {
  width: 20%;
  margin-top: 5px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>