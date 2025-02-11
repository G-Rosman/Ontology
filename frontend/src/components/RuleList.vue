<template>
  <div class="rules-container">
      <h2 class="section-title">Rules</h2>
      
      <table class="rules-table">
          <thead>
              <tr>
                  <th>Rule</th>
                  <th>Actions</th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="rule in rules" :key="rule.id">
                  <td class="rule-content">
                      <div class="rule-item">
                          <label>Directions:</label>
                          <input 
                              v-model="rule.directions"
                              type="text"
                              class="rule-input"
                              @change="updateRule(rule)"
                          >
                      </div>
                      <div class="rule-item">
                          <label>Relations:</label>
                          <input 
                              v-model="rule.relations"
                              type="text"
                              class="rule-input"
                              @change="updateRule(rule)"
                          >
                      </div>
                      <div class="rule-item">
                          <label>Quantors:</label>
                          <input 
                              v-model="rule.quantors"
                              type="text"
                              class="rule-input"
                              @change="updateRule(rule)"
                          >
                      </div>
                      <div class="rule-separator">→</div>
                      <div class="rule-item">
                          <label>Result Direction:</label>
                          <input 
                              v-model="rule.res_direction"
                              type="text"
                              class="rule-input"
                              @change="updateRule(rule)"
                          >
                      </div>
                      <div class="rule-item">
                          <label>Result Relation:</label>
                          <input 
                              v-model="rule.res_relation"
                              type="text"
                              class="rule-input"
                              @change="updateRule(rule)"
                          >
                      </div>
                      <div class="rule-item">
                          <label>Result Quantor:</label>
                          <input 
                              v-model="rule.res_quantor"
                              type="text"
                              class="rule-input"
                              @change="updateRule(rule)"
                          >
                      </div>
                  </td>
                  <td class="actions">
                      <button class="action-button" @click="saveRule(rule)">
                          Save
                      </button>
                      <button class="action-button danger" @click="deleteRule(rule.id)">
                          Delete
                      </button>
                  </td>
              </tr>
          </tbody>
      </table>
  
      <button class="create-button" @click="createRule">
          Create New Rule
      </button>
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
              try {
                  const response = await axios.get('/api/rules');
                  this.rules = response.data;
              } catch (error) {
                  console.error('Error fetching rules:', error);
              }
          },
          
          async updateRule(rule) {
              try {
                  const response = await axios.put(`/api/update/rule/${rule.id}`, rule);
                  this.rules = this.rules.map(r =>
                      r.id === rule.id ? response.data : r
                  );
                  console.log('Rule updated successfully:', response.data);
              } catch (error) {
                  console.error('Error updating rule:', error);
                  if (error.response) {
                      console.error('Server response:', error.response.data);
                  }
              }
          },
          
          async saveRule(rule) {
              await this.updateRule(rule);
          },
          
          async deleteRule(id) {
              try {
                  await axios.delete(`/api/delete/rule/${id}`);
                  await this.fetchRules();
              } catch (error) {
                  console.error('Error deleting rule:', error);
              }
          },
          
          createRule() {
              this.$emit('create-rule');
          }
      }
  };
  </script>
  
  <style scoped>
  .rules-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
  }
  
  .section-title {
      text-align: center;
      margin: 2rem 0;
      font-size: 1.75rem;
      color: #333;
  }
  
  .rules-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 2rem;
      background-color: #fff;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      overflow: hidden;
  }
  
  .rules-table th,
  .rules-table td {
      padding: 1rem;
      text-align: left;
      border-bottom: 1px solid #e9ecef;
  }
  
  .rules-table th {
      background-color: #f8f9fa;
      font-weight: 600;
      color: #495057;
  }
  
  .rule-content {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
  }
  
  .rule-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
  }
  
  .rule-input {
      padding: 0.25rem 0.5rem;
      border: 1px solid #e9ecef;
      border-radius: 4px;
      font-size: 0.9rem;
  }
  
  .rule-input:focus {
      outline: none;
      border-color: #42b883;
      box-shadow: 0 0 0 2px rgba(66, 184, 131, 0.25);
  }
  
  .rule-separator {
      margin: 0.5rem 0;
      font-weight: bold;
  }
  
  .actions {
      display: flex;
      gap: 0.5rem;
      justify-content: flex-end;
  }
  
  .action-button {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.9rem;
      transition: all 0.3s ease;
  }
  
  .action-button:not(.danger):hover {
      transform: translateY(-1px);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .action-button:not(.danger) {
      background-color: #007bff;
      color: white;
  }
  
  .action-button.danger {
      background-color: #dc3545;
      color: white;
  }
  
  .action-button.danger:hover {
      background-color: #c82333;
  }
  
  .create-button {
      display: block;
      margin: 0 auto;
      padding: 0.75rem 1.5rem;
      background-color: #42b883;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 1rem;
      transition: background-color 0.2s;
  }
  
  .create-button:hover {
      background-color: #2b8a5c;
  }
  </style>