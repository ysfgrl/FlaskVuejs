<template>
  <VueSidebarMenuAkahon v-if="isShow"
    :menu-items="menuItems"
    :menu-title="menuTitle"
    :menu-logo="menuLogo"
    :is-search="isSearch"
    :is-menu-open="false"
    :profile-img="profileImg"
    :profile-name="profileName"
    :profile-role="profileRole"
    :is-exit-button="isExitButton"
    @button-exit-clicked="logout"
  />
</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";

export default {
  name: "LeftMenu",
  components: { VueSidebarMenuAkahon },
  props:['isShow'],
  methods: {
    logout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("isLogin");
      localStorage.removeItem("user");
      location.reload("/Login");
    },
  },
  data() {
    return {
      menuItems: [
        {
          link: "/PersonList",
          name: "Personel Listesi",
          icon: "bx-grid-alt",
        },
      ],
      menuTitle: "Flask Vuejs",
      menuLogo: "/favicon.ico",
      profileName: "Yusuf Uğurlu",
      profileImg: "/profile.jpeg",
      profileRole: "Bilgisayar Mühendisi",
      isExitButton: true,
      isSearch: false,
    };

  },
  created() {
    var isLogin = localStorage.getItem("isLogin");
    if(isLogin == "true"){
      var user = JSON.parse(localStorage.getItem("user"));
      this.profileName = user["username"];
      this.profileRole = user["name"] + " " + user["surname"]
    }
  }
};
</script>

<style scoped></style>
