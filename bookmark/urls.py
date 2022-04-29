from django.urls import path

from bookmark import views
from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, \
    BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    # 클래스만 쓸때는 괄호가 있고, 함수일때는 괄호가 없다. -> as_View()를 통해 함수이름을 가져오기때문
    path('',BookmarkListView.as_view(), name='list'),
    path('add/',BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name="detail"),
    path('edit/<int:pk>/', BookmarkUpdateView.as_view(), name="edit"),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name="delete"),
]


# input
# INF

# n,m
# start
# graph
# distance

# m만큼 입력받기 : 반복
# distance[a].append([b,c])

# 다익스트라 함수
    # q = []
    # start 세팅하기
    # heapq.heappush(q,(0, start)

    # while q:
        # 가져오기 : dist, now = heapq.heappop(q)
        #