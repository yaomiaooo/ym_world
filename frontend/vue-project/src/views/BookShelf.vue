<template>
  <div class="book-shelf">
    <h2>我的文章收藏</h2>
    
    <!-- 添加新文章按钮 -->
    <button @click="showAddForm = true" class="add-btn">
      + 添加新文章
    </button>

    <!-- 添加文章表单 -->
    <div v-if="showAddForm" class="article-form">
      <h3>{{ editingArticle ? '编辑文章' : '添加新文章' }}</h3>
      
      <div class="form-group">
        <label>标题</label>
        <input v-model="currentArticle.title" placeholder="输入文章标题">
      </div>
      
      <div class="form-group">
        <label>封面图片</label>
        <input 
          type="file" 
          @change="handleCoverUpload" 
          accept="image/*"
          class="cover-upload"
        >
        <div v-if="currentArticle.coverPreview" class="cover-preview">
          <img :src="currentArticle.coverPreview" alt="封面预览">
        </div>
      </div>
      
      <div class="form-group">
        <label>内容</label>
        <textarea 
          v-model="currentArticle.content" 
          placeholder="输入文章内容..."
          rows="8"
        ></textarea>
      </div>
      
      <div class="form-group">
        <label>分类</label>
        <select v-model="currentArticle.category">
          <option value="技术">技术</option>
          <option value="文学">文学</option>
          <option value="生活">生活</option>
          <option value="其他">其他</option>
        </select>
      </div>
      
      <div class="form-actions">
        <button @click="saveArticle" class="save-btn">
          {{ editingArticle ? '保存更改' : '添加文章' }}
        </button>
        <button @click="cancelEdit" class="cancel-btn">取消</button>
      </div>
    </div>

    <!-- 文章列表 -->
    <div class="article-list">
      <div 
        v-for="article in articles" 
        :key="article.id" 
        class="article-card"
        @click="viewArticle(article)"
      >
        <div class="article-cover" v-if="article.cover">
          <img :src="article.cover" :alt="article.title">
        </div>
        <div class="article-info">
          <h3>{{ article.title }}</h3>
          <span class="category">{{ article.category }}</span>
          <p class="excerpt">{{ article.content.substring(0, 100) }}{{ article.content.length > 100 ? '...' : '' }}</p>
          <div class="article-meta">
            <span>{{ formatDate(article.created_at) }}</span>
          </div>
        </div>
        <div class="article-actions">
          <button @click.stop="editArticle(article)" class="edit-btn">编辑</button>
          <button @click.stop="deleteArticle(article.id)" class="delete-btn">删除</button>
        </div>
      </div>
    </div>

    <!-- 文章详情模态框 -->
    <div v-if="viewingArticle" class="article-modal" @click.self="viewingArticle = null">
      <div class="modal-content">
        <button @click="viewingArticle = null" class="close-btn">×</button>
        <h2>{{ viewingArticle.title }}</h2>
        <div class="modal-meta">
          <span class="category">{{ viewingArticle.category }}</span>
          <span>{{ formatDate(viewingArticle.created_at) }}</span>
        </div>
        <div v-if="viewingArticle.cover" class="modal-cover">
          <img :src="viewingArticle.cover" :alt="viewingArticle.title">
        </div>
        <div class="modal-content-text">
          <p>{{ viewingArticle.content }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 文章数据结构
const articles = ref([])
const currentArticle = ref({
  title: '',
  cover: null,
  coverPreview: null,
  content: '',
  category: '技术'
})
const editingArticle = ref(null)
const viewingArticle = ref(null)
const showAddForm = ref(false)

// 从本地存储加载数据
/*onMounted(() => {
  const saved = localStorage.getItem('myArticles')
  if (saved) {
    articles.value = JSON.parse(saved)
  }
})*/

onMounted(() => {
  // 从Django接口获取文章列表
  axios.get('http://localhost:8000/studio/articles/')
    .then(response => {
      articles.value = response.data;  // 把接口返回的数据存到articles数组
    })
    .catch(error => {
      console.error('加载文章失败', error);
    });
});

// 处理封面图片上传
const handleCoverUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      currentArticle.value.coverPreview = e.target.result
      currentArticle.value.cover = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

// 保存文章
const saveArticle = () => {
  if (!currentArticle.value.title || !currentArticle.value.content) {
    alert('标题和内容不能为空');
    return;
  }

  // 如果是编辑现有文章，用PUT请求；新增用POST
  const request = editingArticle.value 
    ? axios.put(`http://localhost:8000/studio/articles/${editingArticle.value.id}/`, currentArticle.value)
    : axios.post('http://localhost:8000/studio/articles/', currentArticle.value);

  request.then(() => {
    // 保存成功后，重新加载文章列表
    axios.get('http://localhost:8000/studio/articles/')
      .then(response => {
        articles.value = response.data;
      });
    resetForm();  // 重置表单
  }).catch(error => {
    console.error('保存失败', error);
  });
};

// 编辑文章
const editArticle = (article) => {
  currentArticle.value = {
    title: article.title,
    cover: article.cover,
    coverPreview: article.cover,
    content: article.content,
    category: article.category
  }
  editingArticle.value = article
  showAddForm.value = true
}

// 查看文章详情
const viewArticle = (article) => {
  viewingArticle.value = article
}

// 删除文章
const deleteArticle = (id) => {
  if (confirm('确定要删除吗？')) {
    axios.delete(`http://localhost:8000/studio/articles/${id}/`)
      .then(() => {
        // 删除成功后，重新加载文章列表
        axios.get('http://localhost:8000/studio/articles/')
          .then(response => {
            articles.value = response.data;
          });
      })
      .catch(error => {
        console.error('删除失败', error);
      });
  }
};

// 取消编辑
const cancelEdit = () => {
  resetForm()
}

// 重置表单
const resetForm = () => {
  currentArticle.value = {
    title: '',
    cover: null,
    coverPreview: null,
    content: '',
    category: '技术'
  }
  editingArticle.value = null
  showAddForm.value = false
}

// 保存到本地存储
const saveToLocalStorage = () => {
  localStorage.setItem('myArticles', JSON.stringify(articles.value))
}

// 格式化日期
const formatDate = (date) => {
  // 如果日期为空或无效，返回友好提示
  if (!date) return "无日期";
  
  const validDate = new Date(date);
  // 检查日期是否有效（invalid date 的时间戳是 NaN）
  if (isNaN(validDate.getTime())) {
    return "日期格式错误";
  }
  
  // 有效日期则正常格式化
  return validDate.toLocaleDateString();
};
</script>

<style scoped>
.book-shelf {
  padding: 20px;
  max-width: 1000px;
  margin: 0 auto;
}

.add-btn {
  padding: 10px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 20px;
}

.add-btn:hover {
  background-color: #45a049;
}

.article-form {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input[type="text"],
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-group textarea {
  min-height: 150px;
}

.cover-upload {
  margin-top: 5px;
}

.cover-preview {
  margin-top: 10px;
}

.cover-preview img {
  max-width: 200px;
  max-height: 200px;
  border-radius: 4px;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 15px;
}

.save-btn {
  padding: 8px 16px;
  background-color: #2196F3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.cancel-btn {
  padding: 8px 16px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.article-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.article-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s;
}

.article-card:hover {
  transform: translateY(-5px);
}

.article-cover {
  height: 180px;
  overflow: hidden;
}

.article-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.article-info {
  padding: 15px;
}

.article-info h3 {
  margin: 0 0 5px 0;
  font-size: 1.1rem;
}

.category {
  display: inline-block;
  background-color: #e0f7fa;
  color: #00838f;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8rem;
  margin-bottom: 10px;
}

.excerpt {
  color: #666;
  margin: 10px 0;
  font-size: 0.9rem;
}

.article-meta {
  font-size: 0.8rem;
  color: #999;
}

.article-actions {
  display: flex;
  padding: 10px 15px;
  border-top: 1px solid #eee;
  gap: 10px;
}

.edit-btn {
  padding: 5px 10px;
  background-color: #FFC107;
  color: #333;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
}

.delete-btn {
  padding: 5px 10px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
}

.article-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background: white;
  border-radius: 8px;
  max-width: 800px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  padding: 30px;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #666;
}

.modal-meta {
  display: flex;
  gap: 15px;
  margin: 10px 0 20px;
  color: #666;
}

.modal-cover {
  margin-bottom: 20px;
}

.modal-cover img {
  max-width: 100%;
  max-height: 300px;
  border-radius: 4px;
}

.modal-content-text {
  line-height: 1.6;
  white-space: pre-line;
}
</style>