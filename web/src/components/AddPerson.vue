<template>
  <!-- Start of Modal 1 -->
  <b-modal
    ref="addPersonModal"
    id="person-add-modal"
    title="Yeni Personel Ekle"
    hide-backdrop
    hide-footer
  >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group
        id="form-title-group"
        label="Tc:"
        label-for="form-title-input"
      >
        <b-form-input
          id="form-title-input"
          type="number"
          v-model="addPersonForm.tckn"
          required
          placeholder="tc girin"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group
        id="form-title-group"
        label="İsim:"
        label-for="form-title-input"
      >
        <b-form-input
          id="form-title-input"
          type="text"
          v-model="addPersonForm.name"
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
          v-model="addPersonForm.surname"
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
          v-model="addPersonForm.username"
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
          v-model="addPersonForm.password"
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
  name: "AddPerson",
  data() {
    return {
      addPersonForm: {
        tckn: "",
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
        this.$refs.addPersonModal.show();
      } else {
        this.$refs.addPersonModal.hide();
      }
    },
    addPerson(payload) {
      const path = localStorage.getItem("apiUrl") + "Person/Add";
      axios
        .post(path, payload, {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("access_token"),
          },
        })
        .then(() => {
          this.getPersonList();

          // for message alert
          this.message = "Person Eklendi";

          // to show message when game is added
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getPersonList();
        });
    },

    // 5 initForm - add ediForm after the update method
    initForm() {
      this.addPersonForm.tckn = "";
      this.addPersonForm.name = "";
      this.addPersonForm.surname = "";
      this.addPersonForm.username = "";
      this.addPersonForm.password = "";
    },

    // 3 Submit form validator in the template @submit="onSubmit"
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addPersonModal.hide();
      const payload = {
        tckn: this.addPersonForm.tckn,
        name: this.addPersonForm.name,
        surname: this.addPersonForm.surname,
        username: this.addPersonForm.username,
        password: this.addPersonForm.password,
      };
      this.addPerson(payload);
      this.initForm();
    },

    // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addPersonModal.hide();
      this.initForm();
    },
  },
};
</script>

<style scoped></style>
