from django.shortcuts import render
from .forms import Form
from .models import Article

# Create your views here.
def write(request):
    # 비지니스 로직 구현
    # request, html 템플릿 파일, data
    # hello1 = "hello django"
    # hello2 = "알고보니 쉬운 django"
    # return render(request, 'write.html', {'data1' : hello1, 'data2' : hello2})
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'write.html', {'form' : form})

def articleList(request):
    article_list = Article.objects.all() # 모두 가져오기
    return render(request, 'list.html', {'article_list' : article_list})