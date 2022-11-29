from django.forms import ModelForm
from .models import Article

class Form(ModelForm):
    class Meta:
        # request의 post가 True이면
        # 사용자가 입력한 form 데이터를 변수에 저장
        # ORM으로 DB에 저장

        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email'] # 입력 받을 내용
        # cdate는 자동 생성이기 때문에 넣지 않는다.
        