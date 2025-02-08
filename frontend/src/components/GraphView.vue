<template>
    <div>
      <h2>Graph</h2>
      <img :src="graphImage" alt="Graph" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        graphImage: '',
      };
    },
    async created() {
      await this.fetchGraph();
    },
    methods: {
      async fetchGraph() {
        try {
          const response = await axios.get('/api/graph', { responseType: 'blob' });
          this.graphImage = URL.createObjectURL(response.data);
        } catch (error) {
          console.error('Error fetching graph:', error);
        }
      },
    },
  };
  </script>