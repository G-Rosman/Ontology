<template>
  <div class="rules-container">
      <h2 class="form-title">{{ isEdit ? 'Edit Rule' : 'Create Rule' }}</h2>
      
      <form @submit.prevent="submitForm" class="rules-form">
          <div class="form-group">
              <label for="directions" class="form-label">Directions:</label>
              <input 
                  id="directions"
                  v-model="localRule.directions"
                  type="text"
                  class="form-input"
                  required
              />
          </div>
  
          <div class="form-group">
              <label for="relations" class="form-label">Relations:</label>
              <input 
                  id="relations"
                  v-model="localRule.relations"
                  type="text"
                  class="form-input"
                  required
              />
          </div>
  
          <div class="form-group">
              <label for="quantors" class="form-label">Quantors:</label>
              <input 
                  id="quantors"
                  v-model="localRule.quantors"
                  type="text"
                  class="form-input"
                  required
              />
          </div>
  
          <div class="form-group">
              <label for="res_direction" class="form-label">Result Direction:</label>
              <input 
                  id="res_direction"
                  v-model="localRule.res_direction"
                  type="text"
                  class="form-input"
                  required
              />
          </div>
  
          <div class="form-group">
              <label for="res_relation" class="form-label">Result Relation:</label>
              <input 
                  id="res_relation"
                  v-model="localRule.res_relation"
                  type="text"
                  class="form-input"
                  required
              />
          </div>
  
          <div class="form-group">
              <label for="res_quantor" class="form-label">Result Quantor:</label>
              <input 
                  id="res_quantor"
                  v-model="localRule.res_quantor"
                  type="text"
                  class="form-input"
                  required
              />
          </div>
  
          <button 
              type="submit" 
              class="submit-button"
          >
              {{ isEdit ? 'Update' : 'Create' }}
          </button>
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
      
      data() {
          return {
              localRule: { ...this.rule },
          };
      },
      
      watch: {
          rule: {
              handler(newVal) {
                  this.localRule = { ...newVal };
              },
              deep: true,
          },
      },
      
      methods: {
          async submitForm() {
              const url = this.isEdit ? `update/rule/${this.localRule.id}` : '/api/rule';
              const method = this.isEdit ? 'put' : 'post';
              try {
                  const response = await axios[method](url, this.localRule);
                  this.$emit('rule-saved', response.data);
              } catch (error) {
                  console.error('Error saving rule:', error);
              }
          },
      },
  };
  </script>
  
  <style scoped>
  .rules-container {
      max-width: 600px;
      margin: 0 auto;
      padding: 2rem;
      background-color: #fff;
      border-radius: 12px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .form-title {
      text-align: center;
      margin-bottom: 2rem;
      font-size: 1.75rem;
      color: #333;
  }
  
  .rules-form {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
  }
  
  .form-group {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
  }
  
  .form-label {
      font-weight: 500;
      color: #495057;
  }
  
  .form-input {
      padding: 0.75rem;
      border: 1px solid #e9ecef;
      border-radius: 4px;
      font-size: 1rem;
      transition: border-color 0.3s ease;
  }
  
  .form-input:focus {
      outline: none;
      border-color: #42b883;
      box-shadow: 0 0 0 2px rgba(66, 184, 131, 0.25);
  }
  
  .submit-button {
      display: block;
      margin-top: 1.5rem;
      padding: 0.75rem 1.5rem;
      background-color: #42b883;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 1rem;
      transition: background-color 0.2s;
      align-self: center;
  }
  
  .submit-button:hover {
      background-color: #2b8a5c;
  }
  </style>