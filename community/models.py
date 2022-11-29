from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50) # 컬럼 이름
    contents = models.TextField() # varchar
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True) # 데이터가 생성되는 시스템 시간