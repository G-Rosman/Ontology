<template>
    <div>
      <h2>Links</h2>
      <ul>
        <li v-for="link in links" :key="link.id">
          {{ link.name_start }} -> {{ link.name_end }}
          <button @click="editLink(link)">Edit</button>
          <button @click="deleteLink(link.id)">Delete</button>
        </li>
      </ul>
      <button @click="createLink">Create New Link</button>
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
        const response = await axios.get('/api/links');
        this.links = response.data;
      },
      createLink() {
        this.$emit('create-link');
      },
      editLink(link) {
        this.$emit('edit-link', link);
      },
      async deleteLink(id) {
        try {
          await axios.delete(`/delete/link/${id}`);
          await this.fetchLinks();
        } catch (error) {
          console.error('Error deleting link:', error);
        }
      },
    },
  };
  </script>