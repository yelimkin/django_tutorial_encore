from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm

# 클래스형 뷰
class UserCreateView(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    # 폼에 입력된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL 지정
    success_url = reverse_lazy('register_done')
    # URL 패턴 전달 인자, urls.py 모듈이 메모리에 로딩된 후에 실행

class UserCreateDoneTV(TemplateView): # 성공하고 나면 보일 파일
    template_name = 'registration/register_done.html'