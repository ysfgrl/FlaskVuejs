/* eslint-disable no-console, no-control-regex*/
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
// install bootstrap first
import "bootstrap/dist/css/bootstrap.css";
import "boxicons";
import "datatables-bootstrap";
import "@andresouzaabreu/vue-data-table/dist/DataTable.css";
import "font-awesome/css/font-awesome.min.css";
// Importing the bootstrapvue library
import BootstrapVue from "bootstrap-vue";
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import DataTable from "@andresouzaabreu/vue-data-table";

Vue.config.productionTip = false;
Vue.config.silent = true;

Vue.use(BootstrapVue);
Vue.component("vue-sidebar-menu-akahon", VueSidebarMenuAkahon);
Vue.component("data-table", DataTable);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");