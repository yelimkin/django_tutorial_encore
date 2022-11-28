from django.shortcuts import render

# Create your views here.
def write(request):
    # 비지니스 로직 구현
    # request, html 템플릿 파일, data
    hello1 = "hello django"
    hello2 = "알고보니 쉬운 django"
    return render(request, 'write.html', {'data1' : hello1, 'data2' : hello2})