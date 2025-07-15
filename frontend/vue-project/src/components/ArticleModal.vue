<template>
  <div class="article-modal">
    <div class="modal-content">
      <button @click="$emit('close')" class="close-btn">×</button>
      
      <h2>{{ article.title }}</h2>
      
      <div class="meta">
        <span class="category">{{ article.category }}</span>
        <span class="date">{{ formatDate(article.createdAt) }}</span>
      </div>
      
      <div v-if="article.cover" class="cover">
        <img :src="article.cover" :alt="article.title">
      </div>
      
      <div class="content" v-html="renderedContent"></div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { marked } from 'marked'

const props = defineProps({
  article: Object
})

const renderedContent = computed(() => {
  return marked(props.article.content || '')
})

const formatDate = (date) => {
  return new Date(date).toLocaleString()
}
</script>