import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: {
      token: "",
      isAuthenticated: false,
    },
  }),
  actions: {
    initializeStore() {
      if (localStorage.getItem("token")) {
        this.user.token = localStorage.getItem("token");
        this.user.isAuthenticated = true;
      } else {
        this.user.token = "";
        this.user.isAuthenticated = false;
      }
    },
    setToken(token) {
      this.user.token = token;
      this.user.isAuthenticated = true;
    },
    removeToken() {
      this.user.token = "";
      this.user.isAuthenticated = false;
    },
  },
});
