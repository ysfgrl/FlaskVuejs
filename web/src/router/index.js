import Vue from "vue";
import VueRouter from "vue-router";
import ParsonList from "../components/PersonList";
import LoginPage from "../components/LoginPage";
Vue.use(VueRouter);

localStorage.setItem("apiUrl", "http://localhost:9005/");
const routes = [
  {
    path: "/PersonList",
    name: "PersonList",
    component: ParsonList,
  },
  {
    path: "/Login",
    name: "Login",
    component: LoginPage,
  },
  { path: "*", redirect: "/" },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ["/Login"];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem("access_token");

  if (loggedIn && !authRequired) {
    return next("/PersonList");
  }

  if (authRequired && !loggedIn) {
    return next("/Login");
  }

  next();
});
export default router;
