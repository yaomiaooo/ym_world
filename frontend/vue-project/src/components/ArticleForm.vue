<template>
  <div class="article-form">
    <h3>{{ isEditing ? '编辑文章' : '添加新文章' }}</h3>
    
    <div class="form-group">
      <label>标题</label>
      <input v-model="localArticle.title" placeholder="输入文章标题">
    </div>
    
    <div class="form-group">
      <label>封面图片</label>
      <input type="file" @change="handleCoverUpload">
      <img v-if="localArticle.cover" :src="localArticle.cover" class="cover-preview">
    </div>
    
    <div class="form-group">
      <label>内容</label>
      <QuillEditor 
        v-model:content="localArticle.content" 
        contentType="html"
        theme="snow"
        :options="editorOptions"
      />
    </div>
    
    <div class="form-group">
      <label>标签 (用逗号分隔)</label>
      <input v-model="tagInput" placeholder="例如: 技术,Vue,前端">
    </div>
    
    <div class="form-group">
      <label>分类</label>
      <select v-model="localArticle.category">
        <option value="技术">技术</option>
        <option value="文学">文学</option>
        <option value="生活">生活</option>
      </select>
    </div>
    
    <div class="form-actions">
      <button @click="save" class="save-btn">保存</button>
      <button @click="cancel" class="cancel-btn">取消</button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'

const props = defineProps({
  article: Object,
  isEditing: Boolean
})

const emit = defineEmits(['save', 'cancel'])

const localArticle = ref({...props.article})
const tagInput = ref(props.article.tags?.join(',') || '')

const editorOptions = {
  modules: {
    toolbar: [
      ['bold', 'italic', 'underline'],
      [{ 'list': 'ordered'}, { 'list': 'bullet' }],
      ['link', 'image'],
      ['code-block']
    ]
  }
}

const handleCoverUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      localArticle.value.cover = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const save = () => {
  // 处理标签
  localArticle.value.tags = tagInput.value
    .split(',')
    .map(tag => tag.trim())
    .filter(tag => tag.length > 0)
  
  emit('save', localArticle.value)
}

const cancel = () => {
  emit('cancel')
}
</script>