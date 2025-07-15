from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class Novel(models.Model):

    # ForeignKey：外键，指向另一个模型
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)

    # CharField：短文本字段，max_length必须指定
    title = models.CharField("小说标题", max_length=100, help_text="请输入标题")
    
    # TextField：长文本，blank=True允许为空
    content = models.TextField("内容", blank=True)
    
    # auto_now_add：创建时自动设置时间
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    
    # auto_now：每次保存时更新时间
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        verbose_name = "小说"        # 单数名称
        verbose_name_plural = "小说" # 复数名称（中文通常相同）
        ordering = ['-created_at']  # 默认按创建时间倒序

    def __str__(self):
        return f"{self.title}（ID:{self.id}）"



from django.utils import timezone

# class Article(models.Model):
#     title = models.CharField(max_length=200) #标题
#     cover = models.ImageField(upload_to='covers/', null=True, blank=True) #封面
#     content = models.TextField() #内容
#     category = models.CharField(max_length=50, choices=[
#         ('tech', '技术'),
#         ('literature', '文学'),
#         ('life', '生活')
#     ])#分类
#     tags = models.JSONField(default=list)  #标签，存储为JSON数组
#     is_favorite = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.title

from django.db import models
import uuid

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('tech', '技术'),
        ('life', '生活'),
        ('other', '其他'),
    ]
    
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    cover = models.TextField(null=True, blank=True)  # 存储 base64 编码的图片
    content = models.TextField()
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tech')
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title