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
    # start 세팅하기 : distance[start]=0
    # heapq.heappush(q,(0, start)

    # while q:
        # 가져오기 : dist, now = heapq.heappop(q)
        # 처리했는지 if : distance[now] < dist
            # 했으면 continue
            
        # 현재 노드와 인접한 노드들 거리 처리하기
        # for i in graph[now] : 인접한 것들 모두 가져오기
            # cost = dist + i[1] : 현재노드까지거리 +  현재에서 글로 가는 거리
            # cost < distance[i[0]] : 더 적으면
                # distance[i[0]] = cost
                # heapq.heappush(q, (cost, i[0])
