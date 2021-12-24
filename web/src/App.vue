<template>
  <div id="app">
    <LeftMenu :isShow="isShow"  />
    <TitlePanel />
    <router-view />
    <FooterPanel />
  </div>
</template>

<style>
#app {
  margin-top: 60px;
}
</style>
<script>
import LeftMenu from "./components/LeftMenu";
import TitlePanel from "./components/titlePanel";
import FooterPanel from "./components/footerPanel";
export default {
  data() {
    return {
      isShow:false
    }
  },
  methods:{
  },
  created() {
    var isLogin = localStorage.getItem("isLogin");
    if(isLogin == "true"){
      this.isShow = true;
    }else{
      this.isShow = false;
    }
  },
  components: { FooterPanel, TitlePanel, LeftMenu },
};
</script>
