import { defineStore } from "pinia";

export const useShow = defineStore("show", {
  state: () => ({ all: true, wait: true, move: true, complete: true, graph1: true, graph2: true, sido: '', sigungu: '', dong: '', page: 1, add: false, add_check: false, }),
  actions: {
    changeAll() {
      this.all = !this.all
    },
    changeWait() {
      this.wait = !this.wait
    },
    changeMove() {
      this.move = !this.move
    },
    changeComplete() {
      this.complete = !this.complete
    },
    changegraph1() {
      this.graph1 = !this.graph1
    },
    changegraph2() {
      this.graph2 = !this.graph2
    },
    changeLocation(sido: string, sigungu: string, dong: string) {
      this.sido = sido
      this.sigungu = sigungu
      this.dong = dong
    }
  },
  getters: {},
});
