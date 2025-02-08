<template>
    <div>
      <h1>Welcome to Ontology App</h1>
      <nav>
        <router-link to="/links">Links</router-link> |
        <router-link to="/rules">Rules</router-link> |
        <router-link to="/graph">Graph</router-link>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomeView',
  };
  </script>