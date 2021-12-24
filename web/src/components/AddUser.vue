<template>
  <!-- Start of Modal 1 -->
  <b-modal
    ref="addUserModal"
    id="user-add-modal"
    title="Yeni Kullanıcı"
    hide-backdrop
    hide-footer
  >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group
        id="form-title-group"
        label="İsim:"
        label-for="form-title-input"
      >
        <b-form-input
          id="form-title-input"
          type="text"
          v-model="addUserForm.name"
          required
          placeholder="isim girin"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group
        id="form-genre-group"
        label="Soyisim:"
        label-for="form-genre-input"
      >
        <b-form-input
          id="form-genre-input"
          type="text"
          v-model="addUserForm.surname"
          required
          placeholder="soyisim girin"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group
        id="form-genre-group"
        label="Kullanıcı Adı:"
        label-for="form-genre-input"
      >
        <b-form-input
          id="form-genre-input"
          type="text"
          v-model="addUserForm.username"
          required
          placeholder="kullanıcı adı girin"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group
        id="form-genre-group"
        label="Şifre Adı:"
        label-for="form-genre-input"
      >
        <b-form-input
          id="form-genre-input"
          type="password"
          v-model="addUserForm.password"
          required
          placeholder="şifre girin"
        >
        </b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Ekle</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->
</template>

<script>
import axios from "axios";

export default {
  name: "AddUser",
  data() {
    return {
      addUserForm: {
        name: "",
        surname: "",
        username: "",
        password: "",
      },
    };
  },
  props: ["getPersonList"],
  mounted() {
    // this.open.$on('event',this.openCloseModal);
    // this.open.$on('event',this.openCloseModal);
  },
  ready() {
    // events.$on('eventOpen', () => {
    //   this.parentMsg = `I heard the greeting event from Child component ${++this.counter} times..`;
    // });
  },
  methods: {
    // 2 Add Game Button
    openCloseModal(isOpen) {
      if (isOpen) {
        this.$refs.addUserModal.show();
      } else {
        this.$refs.addUserModal.hide();
      }
    },
    addUser(payload) {
      const path = localStorage.getItem("apiUrl") + "Auth/addUser";
      axios
        .post(path, payload)
        .then(() => {
          this.message = "Person Eklendi";
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // 5 initForm - add ediForm after the update method
    initForm() {
      this.addUserForm.name = "";
      this.addUserForm.surname = "";
      this.addUserForm.username = "";
      this.addUserForm.password = "";
    },

    // 3 Submit form validator in the template @submit="onSubmit"
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addUserModal.hide();
      const payload = {
        name: this.addUserForm.name,
        surname: this.addUserForm.surname,
        username: this.addUserForm.username,
        password: this.addUserForm.password,
      };
      this.addUser(payload);
      this.initForm();
    },

    // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addUserModal.hide();
      this.initForm();
    },
  },
};
</script>

<style scoped></style>
