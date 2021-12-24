<template>
  <div class="vertical-center">
    <div class="container">
      <div class="row ml-lg-5">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">Personel Listesi</div>
            <div class="card-body">
              <b-alert variant="success" v-if="showMessage" show>
                {{ message }}
              </b-alert>
              <!-- Add Game button -->
              <button
                type="button"
                class="btn btn-success btn-sm"
                v-on:click="openPersonAddModal"
              >
                Personel Ekle
              </button>
              <br /><br /><data-table
                v-bind="parametersTable1"
                @actionTriggered="handleAction"
              />
            </div>
          </div>
        </div>
      </div>

      <add-person :getPersonList="getPersonList" ref="addPersonRef" />
      <edit-person :getPersonList="getPersonList" ref="editPersonRef" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import AddPerson from "./AddPerson";
import EditPerson from "./EditPerson";
import TableAction from "./TableAction";
export default {
  components: { EditPerson, AddPerson },
  data() {
    return {
      actionMode: "multiple",

      personList: [],
      editPersonForm: {
        tckn: "",
        name: "",
        surname: "",
        username: "",
        password: "",
      },
      showMessage: false,
    };
  },

  message: "",

  methods: {
    openPersonAddModal() {
      this.$refs.addPersonRef.$refs.addPersonModal.show();
    },
    handleAction(actionName, data) {
      if (actionName == "edit") {
        this.$refs.editPersonRef.showModal(data);
      }
      else if(actionName == "delete"){
        if(confirm("Silinsin mi ?")){
          this.deletePerson(data);
        }
      }
    },
    // 1 GET METHOD
    deletePerson(data){
      const path = localStorage.getItem("apiUrl") + "Person/Delete/" + data["tckn"];
      axios.delete(path, {
              headers: {
                Authorization: "Bearer " + localStorage.getItem("access_token"),
              },
            }
        )
        .then((res) => {
          this.getPersonList()
        })
        .catch(error => {
          console.log(error);
        })
    },
    getPersonList() {
      const path = localStorage.getItem("apiUrl") + "Person/List";
      axios.post(
          path,
          { page: 1, limit: 50 },
          {
            headers: {
              Authorization: "Bearer " + localStorage.getItem("access_token"),
            },
          }
        )
        .then((res) => {
          console.log(res);
          this.personList = res.data.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getPersonList();
  },
  computed: {
    parametersTable1() {
      return {
        data: this.personList,
        columns: [
          {
            key: "tckn",
            title: "TC",
            sortable: false,
          },
          {
            key: "name",
            title: "İsim",
            sortable: false,
          },
          {
            key: "surname",
            title: "Soyisim",
            sortable: false,
          },
          {
            key: "username",
            title: "Kullanıcı Adı",
            sortable: false,
          },
          {
            key: "edit",
            title: "edit",
            sortingFunction: function (a, b) {
              // permissions is an array
              return a.permissions.length - b.permissions.length;
            },
            /* custom component to display the permissions */
            component: TableAction,
          },
        ],
      };
    },
  },
};
</script>
