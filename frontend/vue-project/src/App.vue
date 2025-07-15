<template>
  <div id="app">
    <Sidebar />
    <div class="main-content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import Sidebar from './components/Sidebar.vue'
</script>

<style>
#app {
  display: flex;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  padding: 20px;
  background-color: #fff;
}
</style>