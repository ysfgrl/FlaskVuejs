<template>
  <div class="container">
    <div class="alert alert-info">Mesaj : {{ message }}</div>

    <button
      type="button"
      class="btn btn-success btn-sm"
      v-on:click="openUserAddModal"
    >
      Kullanıcı Ekle
    </button>

    <h2>Login</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label htmlFor="username">Username</label>
        <input
          type="text"
          v-model="username"
          name="username"
          class="form-control"
          :class="{ 'is-invalid': submitted && !username }"
        />
        <div v-show="submitted && !username" class="invalid-feedback">
          Username is required
        </div>
      </div>
      <div class="form-group">
        <label htmlFor="password">Password</label>
        <input
          type="password"
          v-model="password"
          name="password"
          class="form-control"
          :class="{ 'is-invalid': submitted && !password }"
        />
        <div v-show="submitted && !password" class="invalid-feedback">
          Password is required
        </div>
      </div>
      <div class="form-group">
        <button class="btn btn-primary" :disabled="loggingIn">Login</button>
      </div>
    </form>

    <add-user ref="addUserRef" />
  </div>
</template>

<script>
import axios from "axios";
import AddUser from "./AddUser";

export default {
  name: "LoginPage",
  components: { AddUser },
  data() {
    return {
      message: "Giriş Yap",
      username: "",
      password: "",
      submitted: false,
      requestOptions: {
        method: "POST",
        headers: { "Content-Type": "application/json" },
      },
    };
  },
  computed: {
    loggingIn() {
      return false;
    },
  },
  created() {},
  methods: {
    openUserAddModal() {
      this.$refs.addUserRef.$refs.addUserModal.show();
    },
    handleSubmit() {
      this.submitted = true;

      if (this.username && this.password) {
        const path = localStorage.getItem("apiUrl") + `Auth/getToken`;
        axios
          .post(path, { password: this.password, username: this.username })
          .then((res) => {
            console.log(res.data);
            if (res.status == 200 && res.data) {
              this.message = "giriş yapıldı:";
              localStorage.setItem(
                "access_token",
                res.data.data["access_token"]
              );
              localStorage.setItem(
                "user",
                JSON.stringify(res.data.data["user"])
              );
              localStorage.setItem(
                "isLogin",
                "true"
              );
              location.reload("/PersonList");
            } else {
              this.message = "Kullanıcı Adı veya Şifre Yanlış";
            }
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
};
</script>

<style scoped></style>
