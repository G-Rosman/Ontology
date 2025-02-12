<template>
  <div class="links-container">
      <h2 class="section-title">Links</h2>
      
      <table class="links-table">
          <tbody>
              <tr v-for="link in links" :key="link.id">
                  <td class="connection">
                      <div class="property-item">
                          <label>Name Start:</label>
                          <input 
                              v-model="link.name_start"
                              type="text"
                              class="property-input"
                              @change="updateLink(link)"
                          >
                      </div>
                      <div class="property-item">
                          <label>Name End:</label>
                          <input 
                              v-model="link.name_end"
                              type="text"
                              class="property-input"
                              @change="updateLink(link)"
                          >
                      </div>
                  </td>
                  <td class="properties">
                      <div class="property-item">
                          <label>Direction:</label>
                          <input 
                              v-model="link.direction"
                              type="text"
                              class="property-input"
                              @change="updateLink(link)"
                          >
                      </div>
                      <div class="property-item">
                          <label>Relation:</label>
                          <input 
                              v-model="link.relation"
                              type="text"
                              class="property-input"
                              @change="updateLink(link)"
                          >
                      </div>
                      <div class="property-item">
                          <label>Quantor:</label>
                          <input 
                              v-model="link.quantor"
                              type="text"
                              class="property-input"
                              @change="updateLink(link)"
                          >
                      </div>
                      <div class="property-item">
                          <label>Ring:</label>
                          <input 
                              v-model="link.ring"
                              type="number"
                              class="property-input"
                              @change="updateLink(link)"
                          >
                      </div>
                  </td>
                  <td class="actions">
                      <button class="action-button" @click="saveLink(link)">
                          Save
                      </button>
                      <button class="action-button danger" @click="deleteLink(link.id)">
                          Delete
                      </button>
                  </td>
              </tr>
          </tbody>
      </table>
  
      <button class="create-button" @click="createLink">
         Быстрый просмотр
      </button>
  </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
      data() {
          return {
              links: [],
          };
      },
      
      async created() {
          await this.fetchLinks();
      },
      
      methods: {
          async fetchLinks() {
              try {
                  const response = await axios.get('/api/links');
                  this.links = response.data;
              } catch (error) {
                  console.error('Error fetching links:', error);
              }
          },
          
          async updateLink(link) {
              try {
                  const response = await axios.put(`/api/update/link/${link.id}`, link);
                  this.links = this.links.map(l =>
                      l.id === link.id ? response.data : l
                  );
                  console.log('Link updated successfully:', response.data);
              } catch (error) {
                  console.error('Error updating link:', error);
                  if (error.response) {
                      console.error('Server response:', error.response.data);
                  }
              }
          },
          
          async saveLink(link) {
              await this.updateLink(link);
          },
          
          async deleteLink(id) {
              try {
                  await axios.delete(`/api/delete/link/${id}`);
                  await this.fetchLinks();
              } catch (error) {
                  console.error('Error deleting link:', error);
              }
          },
          
          createLink() {
              this.$emit('create-link');
          }
      }
  };
  </script>
  
  <style scoped>
  .links-container {
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
  
  .links-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 2rem;
      background-color: #fff;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      overflow: hidden;
  }
  
  .links-table th,
  .links-table td {
      padding: 1rem;
      text-align: left;
      border-bottom: 1px solid #e9ecef;
  }
  
  .links-table th {
      background-color: #f8f9fa;
      font-weight: 600;
      color: #495057;
  }
  
  .connection {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
  }
  
  .properties {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
  }
  
  .property-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
  }
  
  .property-input {
      padding: 0.25rem 0.5rem;
      border: 1px solid #e9ecef;
      border-radius: 4px;
      font-size: 0.9rem;
  }
  
  .property-input:focus {
      outline: none;
      border-color: #42b883;
      box-shadow: 0 0 0 2px rgba(66, 184, 131, 0.25);
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