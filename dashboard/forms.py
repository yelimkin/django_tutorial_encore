from django.forms import ModelForm
from .models import CountryData

class CountryDataForm(ModelForm):
    class Meta:
        # request의 post가 True이면
        # 사용자가 입력한 form 데이터를 변수에 저장
        # ORM으로 DB에 저장

        model = CountryData
        fields = '__all__'