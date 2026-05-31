import { createApp } from 'vue'
import './index.css'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Feedback from './views/Feedback.vue'
import { Analytics } from "@vercel/analytics/vue"


<Analytics/>

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/feedback', component: Feedback },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

createApp(App).use(router).mount('#root')
