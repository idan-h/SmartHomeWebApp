import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

import ChooseRoom from './components/ChooseRoom.vue'
import Room from './components/Room.vue'
import Other from './components/Other.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', component: ChooseRoom },
  { path: '/other', component: Other },
  { path: '/:id', component: Room },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
