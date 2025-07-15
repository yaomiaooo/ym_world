import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import BookShelf from '../views/BookShelf.vue'
import NovelEditor from '../views/NovelEditor.vue'
import MusicPlayer from '../views/MusicPlayer.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/book-shelf',
    name: 'BookShelf',
    component: BookShelf
  },
  {
    path: '/novel-editor',
    name: 'NovelEditor',
    component: NovelEditor
  },
  {
    path: '/music-player',
    name: 'MusicPlayer',
    component: MusicPlayer
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router