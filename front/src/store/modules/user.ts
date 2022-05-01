import { defineStore } from "pinia";
import axios from "axios";

export const useUser = defineStore("user", {
  state: () => ({ username: '', staff: true, newAlarm: false, }),
  actions: {
    setUsername(username: string) {
      this.username = username
    },
  },
  getters: {}
},
);
