<script setup lang="tsx">
import { Box, ShoppingCartFull, Clock, CircleCheckFilled } from '@element-plus/icons-vue';


const props = defineProps({
  name: String,
  number: Number,
  icon: String,
  // percent: Number,
})
const BoxIcon: JSX.Element = <el-icon color="rgb(115, 150, 211)"><Box /></el-icon>
const WaitIcon: JSX.Element = <el-icon color="rgb(169, 118, 199)"><Clock /></el-icon>
const MovingIcon: JSX.Element = <el-icon color="rgb(255, 145, 0)"><ShoppingCartFull /></el-icon>
const CompleteIcon: JSX.Element = <el-icon color="rgb(76, 163, 76)"><CircleCheckFilled /></el-icon>


</script>

<template>
  <el-card class="w-100 ts-all mb-1">
    <h3 class="name" :class="props.icon">{{ props.name }}</h3>
    <BoxIcon v-if="props.icon === 'Box'" class="icon" :size="60" :class="props.icon"></BoxIcon>
    <WaitIcon v-if="props.icon === 'Wait'" class="icon" :size="60" :class="props.icon"></WaitIcon>
    <MovingIcon v-if="props.icon === 'Move'" class="icon" :size="60" :class="props.icon"></MovingIcon>
    <CompleteIcon v-if="props.icon === 'Complete'" class="icon" :size="60" :class="props.icon"></CompleteIcon>
    <h2 class="number" :class="props.icon">{{ props.number }}</h2>
    <!-- <div class="percent" :class="props.icon">{{ props.percent }}</div> -->
  </el-card>
</template>


<style scoped>
.Box {
  color: rgb(115, 150, 211);
}
.Wait {
  color: rgb(169, 118, 199);
}
.Move {
  color: rgb(255, 145, 0);
}
.Complete {
  color: rgb(76, 163, 76);
}
.icon {
  width: 40%;
}
.number {
  margin-bottom: 2px;
}
.percent {
  font-size: 0.8em;
}
.mb-1 {
  margin-bottom: 1rem;
}
</style>