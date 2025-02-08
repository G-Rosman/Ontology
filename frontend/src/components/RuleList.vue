<template>
    <div>
      <h2>Rules</h2>
      <ul>
        <li v-for="rule in rules" :key="rule.id">
          {{ rule.directions }} | {{ rule.relations }} | {{ rule.quantors }} -> 
          {{ rule.res_direction }} | {{ rule.res_relation }} | {{ rule.res_quantor }}
          <button @click="editRule(rule)">Edit</button>
          <button @click="deleteRule(rule.id)">Delete</button>
        </li>
      </ul>
      <button @click="createRule">Create New Rule</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        rules: [],
      };
    },
    async created() {
      await this.fetchRules();
    },
    methods: {
      async fetchRules() {
        const response = await axios.get('/api/rules');
        this.rules = response.data;
      },
      createRule() {
        this.$emit('create-rule');
      },
      editRule(rule) {
        this.$emit('edit-rule', rule);
      },
      async deleteRule(id) {
        try {
          await axios.delete(`/delete/rule/${id}`);
          await this.fetchRules();
        } catch (error) {
          console.error('Error deleting rule:', error);
        }
      },
    },
  };
  </script>