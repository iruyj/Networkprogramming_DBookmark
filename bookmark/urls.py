from django.urls import path

from bookmark import views
from bookmark.views import BookmarkListView

app_name = 'bookmark'

urlpatterns = [
    # 클래스만 쓸때는 괄호가 있고, 함수일때는 괄호가 없다. -> as_View()를 통해 함수이름을 가져오기때문
    path('list/',BookmarkListView.as_view(), name='list')
]

