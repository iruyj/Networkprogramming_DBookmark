from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from bookmark.models import Bookmark

# 이 클래스는 자동으로 html파일을 연동시키는데 디비의 모든 내용을 연결해 표시해준다.
class BookmarkListView(ListView):
    model = Bookmark
    # 장고가 자동으로 연결한 템플릿 파일 : bookmark_list.html, {'bookmark_list':Bookmark.objects.all()}
