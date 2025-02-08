<template>
    <div>
      <h2>{{ isEdit ? 'Edit Link' : 'Create Link' }}</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label>Name Start:</label>
          <input v-model="link.name_start" required />
        </div>
        <div>
          <label>Direction:</label>
          <input v-model="link.direction" required />
        </div>
        <div>
          <label>Relation:</label>
          <input v-model="link.relation" required />
        </div>
        <div>
          <label>Quantor:</label>
          <input v-model="link.quantor" required />
        </div>
        <div>
          <label>Name End:</label>
          <input v-model="link.name_end" required />
        </div>
        <div>
          <label>Ring:</label>
          <input v-model="link.ring" type="number" required />
        </div>
        <button type="submit">{{ isEdit ? 'Update' : 'Create' }}</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      link: {
        type: Object,
        default: () => ({
          name_start: '',
          direction: '',
          relation: '',
          quantor: '',
          name_end: '',
          ring: 0,
        }),
      },
      isEdit: {
        type: Boolean,
        default: false,
      },
    },
    methods: {
      async submitForm() {
        const url = this.isEdit ? `/update/link/${this.link.id}` : '/api/link';
        const method = this.isEdit ? 'put' : 'post';
        try {
          const response = await axios[method](url, this.link);
          this.$emit('link-saved', response.data);
        } catch (error) {
          console.error('Error saving link:', error);
        }
      },
    },
  };
  </script>