<template>
    <div>
      <LinkList @create-link="showCreateForm" @edit-link="showEditForm" />
      <LinkForm
        v-if="showForm"
        :link="currentLink"
        :isEdit="isEdit"
        @link-saved="handleLinkSaved"
      />
    </div>
  </template>
  
  <script>
  import LinkList from '@/components/LinkList.vue';
  import LinkForm from '@/components/LinkForm.vue';
  
  export default {
    components: {
      LinkList,
      LinkForm,
    },
    data() {
      return {
        showForm: false,
        currentLink: null,
        isEdit: false,
      };
    },
    methods: {
      showCreateForm() {
        this.currentLink = null;
        this.isEdit = false;
        this.showForm = true;
      },
      showEditForm(link) {
        this.currentLink = { ...link };
        this.isEdit = true;
        this.showForm = true;
      },
      handleLinkSaved() {
        this.showForm = false;
        this.currentLink = null;
      },
    },
  };
  </script>