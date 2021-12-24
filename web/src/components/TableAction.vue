<template>
  <div class="action-buttons">
<!--    <button class="btn btn-outline-success" @click="handleAction('view')">-->
<!--      <i class="fa fa-eye"></i>-->
<!--    </button>-->
    <button class="btn btn-outline-primary" @click="handleAction('edit')">
      <i class="fa fa-edit"></i>
    </button>
    <button class="btn btn-outline-dark" @click="handleAction('delete')">
      <i class="fa fa-trash"></i>
    </button>
  </div>
</template>

<script>
export default {
  name: "TableAction",
  methods: {
    handleAction(actionName) {
      this.$parent.$parent.$parent.handleAction(actionName, this.data);
    },
  },
  props: {
    data: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped></style>
