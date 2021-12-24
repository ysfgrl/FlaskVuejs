<template>
  <!-- Start of Modal 2 -->
  <b-modal
    ref="editPersonModal"
    id="game-update-modal"
    title="Update"
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
          v-model="editPersonForm.tckn"
          required
          disabled
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
          v-model="editPersonForm.name"
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
          v-model="editPersonForm.surname"
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
          v-model="editPersonForm.username"
          required
          placeholder="kullanıcı adı girin"
        >
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="outline-info">Güncelle</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- end of modal 2 -->
</template>

<script>
import axios from "axios";

export default {
  name: "EditPerson",
  props: ["getPersonList"],
  data() {
    return {
      editData: {
        tckn: "",
        name: "",
        surname: "",
        username: "",
        password: "",
      },
      editPersonForm: {
        tckn: "",
        name: "",
        surname: "",
        username: "",
      },
    };
  },
  methods: {
    showModal(data) {
      this.editPersonForm = data;
      this.$refs.editPersonModal.show();
    },
    initForm() {
      this.editPersonForm.tckn = "";
      this.editPersonForm.name = "";
      this.editPersonForm.surname = "";
      this.editPersonForm.username = "";
      this.editPersonForm.password = "";
    },

    // 3 Submit form validator in the template @submit="onSubmit"
    onSubmit(e) {
      e.preventDefault();
      this.$refs.editPersonModal.hide();
      const payload = {
        tckn: this.editPersonForm.tckn,
        name: this.editPersonForm.name,
        surname: this.editPersonForm.surname,
        username: this.editPersonForm.username,
      };
      this.updatePerson(payload);
    },

    updatePerson(payload) {
      const path = localStorage.getItem("apiUrl") + "Person/Edit";
      axios
        .put(path, payload, {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("access_token"),
          },
        })
        .then((res) => {
          this.getPersonList();
          this.message = "Personel Güncellendi";
          console.log(res.data);
        })
        .catch((error) => {
          console.error(error);
          this.getPersonList();
        });
    },
    // 5 Handle reset / cancel button click
    onReset(e) {
      e.preventDefault();
      this.$refs.editPersonModal.hide();
      this.initForm();
    },
  },
};
</script>

<style scoped></style>
