<template>
  <div class="container">
    <h1>{{ title }}</h1>

    <!-- 添加角色选择下拉框 -->
    <select v-model="selectedCharacter">
      <option v-for="char in characters" :value="char.id">
        {{ char.name }}
      </option>
    </select>
    
    <!-- 增强的Vditor编辑器 -->
    <div id="editor"></div>

    
    <!-- 带状态提示的保存按钮 -->
    <button @click="save" :disabled="isSaving">
      {{ isSaving ? '保存中...' : '保存' }}
    </button>
    
    <!-- 显示保存结果 -->
    <p v-if="saveMessage" :class="saveStatus">{{ saveMessage }}</p>

    <footer>© 2025 版权所有</footer>


  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Vditor from 'vditor'
import 'vditor/dist/index.css'
import axios from 'axios'

const title = ref('开始创作吧笨鸟大人')
const content = ref('')
const selectedCharacter = ref(1)
const isSaving = ref(false)
const saveMessage = ref('')
const saveStatus = ref('')

// 模拟角色数据
const characters = ref([
  { id: 1, name: '齐司礼' },
  { id: 2, name: '祁煜' }
])

let vditorInstance = null

onMounted(() => {
  vditorInstance = new Vditor('editor', {
    height: 500,
    placeholder: '输入正文...',
    after: () => {
      content.value = vditorInstance.getValue()
    }
  })
})

const save = async () => {
  if (!content.value.trim()) {
    saveMessage.value = '内容不能为空'
    saveStatus.value = 'error'
    return
  }

  isSaving.value = true
  try {
    const response = await axios.post('http://localhost:8000/studio/api/save', {
      title: `【${characters.value.find(c => c.id === selectedCharacter.value).name}】的创作`,
      content: content.value,
      character: selectedCharacter.value
    })
    
    saveMessage.value = `保存成功！ID: ${response.data.id}`
    saveStatus.value = 'success'
  } catch (error) {
    saveMessage.value = `保存失败: ${error.response?.data?.message || error.message}`
    saveStatus.value = 'error'
  } finally {
    isSaving.value = false
  }
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
select {
  margin: 10px 0;
  padding: 5px;
}
button {
  padding: 8px 15px;
  background: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}
button:disabled {
  background: #cccccc;
}
.success { color: green; }
.error { color: red; }
</style>