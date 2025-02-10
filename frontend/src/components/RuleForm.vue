<template>
  <div>
    <h2>{{ isEdit ? 'Edit Rule' : 'Create Rule' }}</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label>Directions:</label>
        <input v-model="localRule.directions" required />
      </div>
      <div>
        <label>Relations:</label>
        <input v-model="localRule.relations" required />
      </div>
      <div>
        <label>Quantors:</label>
        <input v-model="localRule.quantors" required />
      </div>
      <div>
        <label>Result Direction:</label>
        <input v-model="localRule.res_direction" required />
      </div>
      <div>
        <label>Result Relation:</label>
        <input v-model="localRule.res_relation" required />
      </div>
      <div>
        <label>Result Quantor:</label>
        <input v-model="localRule.res_quantor" required />
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
  data() {
    return {
      localRule: { ...this.rule }, // Локальная копия пропса
    };
  },
  watch: {
    rule: {
      handler(newVal) {
        this.localRule = { ...newVal }; // Обновляем локальную копию при изменении пропса
      },
      deep: true,
    },
  },
  methods: {
    async submitForm() {
      const url = this.isEdit ? `/update/rule/${this.localRule.id}` : '/api/rule';
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