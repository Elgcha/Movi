import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("./views/Home.vue"),
  },
  {
    path: "/signup",
    name: "Signup",
    component: () => import("./views/Signup.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("./views/Login.vue"),
  },
  {
    path: "/detail",
    name: "Detail",
    component: () => import("./views/Detail.vue"),
  },
  {
    path: "/movi",
    name: "Movi",
    component: () => import("./views/Movi.vue"),
  },
  {
    path: "/alarm",
    name: "Alarm",
    component: () => import("./views/Alarm.vue"),
  },
  {
    path: "/404",
    name: "404",
    component: () => import("./views/Err404.vue"),
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: "/404"
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;