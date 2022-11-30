from django.shortcuts import render
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def dashboard(request):
    # 나라별 인구 데이터를 DB에서 가져오기
    country_datas = CountryData.objects.all()

    # if request method == post
    #       valid 하다면
    #       폼에 입력한 데이터를 저장
    # else
    #       폼 객체를 생성
    #       폼 객체를 렌더링
    if request.method == 'POST':
        form = CountryDataForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CountryDataForm()

    context = {
        'country_datas': country_datas, 
        'form': form,
    }
    
    return render(request, 'dashboard/dashboard.html', context)
