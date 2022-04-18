from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from bookmark.models import Bookmark

# 이 클래스는 자동으로 html파일을 연동시키는데 디비의 모든 내용을 연결해 표시해준다.
class BookmarkListView(ListView):
    model = Bookmark
    # 장고가 자동으로 연결한 템플릿 파일 : bookmark_list.html, {'bookmark_list':Bookmark.objects.all()}

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name','url']     # '__all__' 로 쓸수도 있다. 생성할 필드들
    template_name_suffix = '_create'# bookmark_form.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')     # 클릭하면이동할 화면


    

