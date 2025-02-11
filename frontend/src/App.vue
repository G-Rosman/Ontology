<template>
  <div id="app">
      <nav class="navbar">
          <div class="navbar-brand">
              <span class="brand-text">Онтологии</span>
          </div>
          
          <div class="navbar-links">
              <router-link to="/links" class="nav-link">Links</router-link>
              <router-link to="/rules" class="nav-link">Rules</router-link>
              <router-link to="/graph" class="nav-link">Graph</router-link>
          </div>
      </nav>
      
      <router-view></router-view>
  </div>
  </template>
  
  <script>
  export default {
      name: 'App',
  };
  </script>
  
  <style>
  #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      color: #2c3e50;
  }
  
  .navbar {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background-color: #2c3e50;
      padding: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      z-index: 1000;
  }
  
  .navbar-brand {
      font-size: 1.5rem;
      color: #fff;
      font-weight: bold;
  }
  
  .navbar-links {
      display: flex;
      gap: 2rem;
  }
  
  .nav-link {
      color: #fff;
      text-decoration: none;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      transition: all 0.3s ease;
  }
  
  .nav-link:hover {
      background-color: #39495e;
  }
  
  .nav-link.router-link-exact-active {
      background-color: #42b883;
  }
  
  .router-view {
      margin-top: 80px;
      padding: 2rem;
  }
  </style>