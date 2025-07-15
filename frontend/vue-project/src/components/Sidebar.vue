<template>
  <div class="sidebar">
    <div class="logo">我的奇思妙想</div>
    <nav>
      <ul>
        <li>
          <router-link to="/" exact-active-class="active">
            <span class="icon">🏠</span>
            <span>首页</span>
          </router-link>
        </li>
        <li>
          <router-link to="/book-shelf" active-class="active">
            <span class="icon">📚</span>
            <span>我的书架</span>
          </router-link>
        </li>
        <li>
          <router-link to="/novel-editor" active-class="active">
            <span class="icon">✍️</span>
            <span>开始创作</span>
          </router-link>
        </li>
        <li>
          <router-link to="/music-player" active-class="active">
            <span class="icon">🎵</span>
            <span>音乐播放器</span>
          </router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script setup>
</script>

<style scoped>
.sidebar {
  width: 250px;
  background-color: #f8f8f8;
  padding: 20px;
  border-right: 1px solid #ddd;
  height: 100vh;
  position: sticky;
  top: 0;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 30px;
  padding: 5px;
  text-align: center;
}

nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

nav li {
  margin-bottom: 10px;
}

nav a {
  display: flex;
  align-items: center;
  padding: 12px 15px;
  text-decoration: none;
  color: #333;
  border-radius: 5px;
  transition: all 0.3s;
}

nav a:hover {
  background-color: #e0e0e0;
}

nav a.active {
  background-color: #007bff;
  color: white;
}

.icon {
  margin-right: 10px;
  font-size: 1.2rem;
}
</style>