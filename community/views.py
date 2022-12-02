from django.shortcuts import render
from .forms import Form
from .models import Article
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.
# def write(request):
#     # 비지니스 로직 구현
#     # request, html 템플릿 파일, data
#     # hello1 = "hello django"
#     # hello2 = "알고보니 쉬운 django"
#     # return render(request, 'write.html', {'data1' : hello1, 'data2' : hello2})
#     if request.method == 'POST':
#         form = Form(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = Form()
#     return render(request, 'community/write.html', {'form' : form})

# def articleList(request):
#     article_list = Article.objects.all() # 모두 가져오기
#     return render(request, 'community/list.html', {'article_list' : article_list})

# def viewDetail(request, num=1):
#     # 클릭한 레코드를 DB 읽어오기
#     article_detail = Article.objects.get(id=num) # 하나 가져오기
#     return render(request, 'community/view_detail.html', {'article_detail':article_detail})

class WriteFormView(CreateView):
    model = Article
    fields = ['name', 'title', 'contents', 'url', 'email']
    template_name = 'community/write.html'
    success_url = reverse_lazy('community:list')

    # 부모 클래스인 CreateView 클래스의 form_valid() 호출을 위해 super()
    # form.save() 실행과 success_url로 리다렉트
    # 유효한 폼 데이터가 POST 요청되었을 때, form_valid가 호출된다.
    # form_valid는 단순히 success_url로의 연결을 수행 
    def form_valid(self, form):
        return super().form_valid(form)

class ArticleListView(ListView):
    model = Article
    template_name = 'community/list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'community/view_detail.html'

def index(request):
    latest_article_list = Article.objects.all().order_by('-cdate')[:3] # 내림차순으로 3개 정렬하기 
    return render(request, 'index.html', {'latest_article_list' : latest_article_list})
