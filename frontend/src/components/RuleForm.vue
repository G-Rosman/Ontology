<template>
    <div>
      <h2>{{ isEdit ? 'Edit Rule' : 'Create Rule' }}</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label>Directions:</label>
          <input v-model="rule.directions" required />
        </div>
        <div>
          <label>Relations:</label>
          <input v-model="rule.relations" required />
        </div>
        <div>
          <label>Quantors:</label>
          <input v-model="rule.quantors" required />
        </div>
        <div>
          <label>Result Direction:</label>
          <input v-model="rule.res_direction" required />
        </div>
        <div>
          <label>Result Relation:</label>
          <input v-model="rule.res_relation" required />
        </div>
        <div>
          <label>Result Quantor:</label>
          <input v-model="rule.res_quantor" required />
        </div>
        <button type="submit">{{ isEdit ? 'Update' : 'Create' }}</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      rule: {
        type: Object,
        default: () => ({
          directions: '',
          relations: '',
          quantors: '',
          res_direction: '',
          res_relation: '',
          res_quantor: '',
        }),
      },
      isEdit: {
        type: Boolean,
        default: false,
      },
    },
    methods: {
      async submitForm() {
        const url = this.isEdit ? `/update/rule/${this.rule.id}` : '/api/rule';
        const method = this.isEdit ? 'put' : 'post';
        try {
          const response = await axios[method](url, this.rule);
          this.$emit('rule-saved', response.data);
        } catch (error) {
          console.error('Error saving rule:', error);
        }
      },
    },
  };
  </script>