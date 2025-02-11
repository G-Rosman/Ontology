<template>
  <div class="graph-container">
      <h2 class="title">Граф</h2>
      
      <div class="image-wrapper">
          <img 
              ref="image"
              :src="graphImage"
              alt="Граф"
              v-if="graphImage"
              @load="handleImageLoad"
              @error="handleImageError"
              class="graph-image"
          />
          
          <div v-else class="loading-state">
              <p>Загрузка графа...</p>
          </div>
  
          <div v-if="error" class="error-message">
              {{ error }}
          </div>
      </div>
  
      <button 
          v-if="graphImage"
          class="save-button"
          @click="saveImage"
      >
          Сохранить изображение
      </button>
  </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
      data() {
          return {
              graphImage: '',
              isLoading: true,
              error: null
          };
      },
      
      async created() {
          await this.fetchGraph();
      },
      
      methods: {
          async fetchGraph() {
              try {
                  this.isLoading = true;
                  const response = await axios.get('/api/graph', {
                      responseType: 'blob',
                      headers: {
                          'Accept': 'image/png'
                      }
                  });
                  
                  const contentType = response.headers['content-type'];
                  if (!contentType || !contentType.includes('image/png')) {
                      throw new Error('Сервер не вернул PNG-изображение');
                  }
                  
                  this.graphImage = URL.createObjectURL(response.data);
              } catch (error) {
                  this.error = error.message || 'Ошибка при загрузке графа';
                  console.error('Error fetching graph:', error);
              } finally {
                  this.isLoading = false;
              }
          },
          
          handleImageLoad() {
              this.isLoading = false;
              this.error = null;
          },
          
          handleImageError() {
              this.error = 'Ошибка при загрузке изображения';
              this.isLoading = false;
          },
          
          saveImage() {
              if (!this.graphImage) return;
              
              const link = document.createElement('a');
              link.href = this.graphImage;
              link.download = 'graph.png';
              
              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
          },
          
          beforeUnmount() {
              if (this.graphImage) {
                  URL.revokeObjectURL(this.graphImage);
              }
          }
      }
  };
  </script>
  
  <style scoped>
  .graph-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
  }
  
  .title {
      text-align: center;
      margin: 2rem 0;
      font-size: 1.75rem;
      color: #333;
  }
  
  .image-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 400px;
      padding: 1rem;
      border-radius: 8px;
      background-color: #f8f9fa;
  }
  
  .graph-image {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 4px;
  }
  
  .loading-state {
      text-align: center;
      color: #666;
      font-size: 1.125rem;
  }
  
  .error-message {
      text-align: center;
      color: #dc3545;
      font-size: 1.125rem;
      padding: 1rem;
      border-radius: 4px;
      background-color: rgba(220, 53, 69, 0.1);
  }
  
  .save-button {
      display: block;
      margin: 1rem auto;
      padding: 0.75rem 1.5rem;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 1rem;
      transition: background-color 0.2s;
  }
  
  .save-button:hover {
      background-color: #0056b3;
  }
  </style>