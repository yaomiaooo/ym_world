<template>
  <div class="home">
    <h1>欢迎来到创作平台！</h1>
    <p class="subtitle">在这里，你可以开始创作你的小说，管理你的书籍，享受音乐。</p>
    
    <div class="feature-cards">
      <div class="card">
        <h3>我的书架</h3>
        <p>管理你的阅读和创作</p>
        <router-link to="/book-shelf" class="btn">查看书架</router-link>
      </div>
      
      <div class="card">
        <h3>开始创作</h3>
        <p>创作属于你的故事</p>
        <router-link to="/novel-editor" class="btn">开始写作</router-link>
      </div>
      
      <div class="card">
        <h3>音乐播放器</h3>
        <p>享受创作时的背景音乐</p>
        <router-link to="/music-player" class="btn">播放音乐</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 10px;
}

.subtitle {
  text-align: center;
  color: #666;
  margin-bottom: 40px;
}

.feature-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.card {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.card h3 {
  margin-top: 0;
  color: #333;
}

.card p {
  color: #666;
  margin-bottom: 20px;
}

.btn {
  display: inline-block;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #0056b3;
}
</style>