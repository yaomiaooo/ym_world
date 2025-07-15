<template>
  <div class="article-card" :class="{ favorite: article.isFavorite }">
    <div class="article-cover" @click="$emit('view', article)">
      <img v-if="article.cover" :src="article.cover" :alt="article.title">
      <div v-else class="cover-placeholder">{{ article.title.charAt(0) }}</div>
    </div>
    
    <div class="article-info">
      <h3 @click="$emit('view', article)">{{ article.title }}</h3>
      
      <div class="tags">
        <span v-for="tag in article.tags" :key="tag">{{ tag }}</span>
      </div>
      
      <div class="actions">
        <button @click.stop="$emit('toggle-favorite', article.id)" class="favorite-btn">
          {{ article.isFavorite ? '★' : '☆' }}
        </button>
        <button @click.stop="$emit('edit', article)" class="edit-btn">编辑</button>
        <button @click.stop="$emit('delete', article.id)" class="delete-btn">删除</button>
      </div>
    </div>
  </div>
</template>