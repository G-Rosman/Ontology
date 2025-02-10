<template>
  <div>
    <h2>{{ isEdit ? 'Edit Link' : 'Create Link' }}</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label>Name Start:</label>
        <input v-model="localLink.name_start" required />
      </div>
      <div>
        <label>Direction:</label>
        <input v-model="localLink.direction" required />
      </div>
      <div>
        <label>Relation:</label>
        <input v-model="localLink.relation" required />
      </div>
      <div>
        <label>Quantor:</label>
        <input v-model="localLink.quantor" required />
      </div>
      <div>
        <label>Name End:</label>
        <input v-model="localLink.name_end" required />
      </div>
      <div>
        <label>Ring:</label>
        <input v-model="localLink.ring" type="number" required />
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
  data() {
    return {
      localLink: { ...this.link }, // Создаем локальную копию пропса
    };
  },
  watch: {
    link: {
      handler(newVal) {
        this.localLink = { ...newVal }; // Обновляем локальную копию при изменении пропса
      },
      deep: true,
    },
  },
  methods: {
    async submitForm() {
      const url = this.isEdit ? `/update/link/${this.localLink.id}` : '/api/link';
      const method = this.isEdit ? 'put' : 'post';
      try {
        const response = await axios[method](url, this.localLink);
        this.$emit('link-saved', response.data);
      } catch (error) {
        console.error('Error saving link:', error);
      }
    },
  },
};
</script>