<template>
  <div class="home-container">
      <header class="hero">
          <h1 class="title">Ontology App</h1>
          <nav class="main-nav">
              <router-link to="/links" class="nav-link">Links</router-link>
              <router-link to="/rules" class="nav-link">Rules</router-link>
              <router-link to="/graph" class="nav-link">Graph</router-link>
          </nav>
      </header>
  </div>
  </template>
  
  <script>
  export default {
      name: 'HomeView',
  };
  </script>
  
  <style scoped>
  .home-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
  }
  
  .hero {
      text-align: center;
      padding: 4rem 0;
      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
      border-radius: 12px;
      margin-bottom: 2rem;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .title {
      font-size: 2.5rem;
      color: #2c3e50;
      margin: 2rem 0;
      font-weight: 700;
  }
  
  .main-nav {
      display: flex;
      justify-content: center;
      gap: 2rem;
  }
  
  .nav-link {
      color: #2c3e50;
      text-decoration: none;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      transition: all 0.3s ease;
      font-size: 1.1rem;
      font-weight: 500;
  }
  
  .nav-link:hover {
      background-color: rgba(255, 255, 255, 0.9);
      transform: translateY(-2px);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .nav-link.router-link-exact-active {
      background-color: #42b883;
      color: white;
      transform: translateY(-2px);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  </style>