from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def dashboard(request):
    # if request method == post
    #       valid 하다면
    #       폼에 입력한 데이터를 저장
    # else
    #       폼 객체를 생성
    #       폼 객체를 렌더링
    if request.method == 'POST':
        form = CountryDataForm(request.POST)
        # print(form)
        if form.is_valid():
            '''
            나라 이름(country)이 DB 값이 있는지 확인
            입력한 나라 이름이 
            있으면 업데이트
            없으면 저장
            '''
            # 폼에 입력한 값을 개별로 변수 대입
            input_country = form.data.get('country', None)
            input_num = form.data.get('population', None)

            CountryData.objects.update_or_create(
                # filter - update
                country = input_country,
                # new value - create
                defaults= {
                    'country' : input_country,
                    'population' : input_num
                })
            # form.save()
            # return redirect('/dashboard')
            return redirect('.')

    else:
        form = CountryDataForm()

    country_datas = CountryData.objects.all()

    context = {
        'country_datas': country_datas, 
        'form': form,
    }
    
    return render(request, 'dashboard/dashboard.html', context)
