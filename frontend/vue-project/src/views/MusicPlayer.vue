<template>
  <div class="music-player">
    <h2>音乐播放器</h2>
    <audio controls>
      <source :src="audioFile" type="audio/mpeg">
      您的浏览器不支持音频元素。
    </audio>
    <div class="controls">
      <button @click="play">播放</button>
      <button @click="pause">暂停</button>
      <input type="range" v-model="volume" min="0" max="1" step="0.1" @input="setVolume">
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import audioFile from '@/assets/audio/lysk.mp3' // 修改为你的实际文件名

const audioRef = ref(null)
const volume = ref(0.7)

const play = () => {
  audioRef.value.play()
}

const pause = () => {
  audioRef.value.pause()
}

const setVolume = () => {
  audioRef.value.volume = volume.value
}
</script>

<style scoped>
.music-player {
  padding: 20px;
  background-color: #f8f8f8;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  margin: 0 auto;
}

.controls {
  margin-top: 15px;
  display: flex;
  gap: 10px;
  align-items: center;
}

button {
  padding: 8px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>