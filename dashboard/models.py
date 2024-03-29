from django.db import models

# Create your models here.
class CountryData(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    class Meta:
        verbose_name_plural = "각 나라별 인구 데이터"
    def __str__(self): # print 함수에 이 클래스의 객체를 넣을 경우, 이 메소드의 리턴값을 출력
        return f"{self.country}--{self.population}"
