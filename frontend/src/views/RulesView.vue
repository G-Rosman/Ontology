<template>
    <div>
      <RuleList @create-rule="showCreateForm" @edit-rule="showEditForm" />
      <RuleForm
        v-if="showForm"
        :rule="currentRule"
        :isEdit="isEdit"
        @rule-saved="handleRuleSaved"
      />
    </div>
  </template>
  
  <script>
  import RuleList from '@/components/RuleList.vue';
  import RuleForm from '@/components/RuleForm.vue';
  
  export default {
    components: {
      RuleList,
      RuleForm,
    },
    data() {
      return {
        showForm: false,
        currentRule: null,
        isEdit: false,
      };
    },
    methods: {
      showCreateForm() {
        this.currentRule = null;
        this.isEdit = false;
        this.showForm = true;
      },
      showEditForm(rule) {
        this.currentRule = { ...rule };
        this.isEdit = true;
        this.showForm = true;
      },
      handleRuleSaved() {
        this.showForm = false;
        this.currentRule = null;
      },
    },
  };
  </script>