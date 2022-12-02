from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50) # 컬럼 이름
    contents = models.TextField() # varchar
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True) # 데이터가 생성되는 시스템 시간
    mdate = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) # 소유자가 삭제되면 글도 삭제

    class Meta:
        verbose_name_plural = "메모 작성하기"
        ordering = ('-mdate',)
    def __str__(self):
        return f"{self.title} -- {self.name} -- {self.cdate}"
    def get_absolute_url(self):
        # 모델의 개별 데이터 url을 문자열로 반환
        return reverse('community:view_detail', args=(self.id,))