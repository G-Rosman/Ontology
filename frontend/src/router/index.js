import Vue from 'vue';
import Router from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LinksView from '@/views/LinksView.vue';
import RulesView from '@/views/RulesView.vue';
import GraphView from '@/views/GraphView.vue';

Vue.use(Router);

export default new Router({
  mode: 'history', // Используем history mode
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/links',
      name: 'links',
      component: LinksView,
    },
    {
      path: '/rules',
      name: 'rules',
      component: RulesView,
    },
    {
      path: '/graph',
      name: 'graph',
      component: GraphView,
    },
  ],
});