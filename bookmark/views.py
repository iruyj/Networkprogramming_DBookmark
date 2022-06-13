from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from accounts.models import Profile
from bookmark.models import Bookmark

# 이 클래스는 자동으로 html파일을 연동시키는데 디비의 모든 내용을 연결해 표시해준다.
class BookmarkListView(ListView):
    model = Bookmark
    # 장고가 자동으로 연결한 템플릿 파일 : bookmark_list.html, {'bookmark_list':Bookmark.objects.all()}
    
    def get_queryset(self):
        user = self.request.user
        # 로그인 하면, 로그인한 사용자의 북마크만 보이기
        if user.is_authenticated:
            #user -> profile -> bookmark
            profile = Profile.objects.get(user=user)
            bookmark_list = Bookmark.objects.filter(profile=profile)
        # 로그인 안하면 북마크 보이지말기
        else:
            bookmark_list = Bookmark.objects.none()
        return bookmark_list

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name','url','profile']     # '__all__' 로 쓸수도 있다. 생성할 필드들
    template_name_suffix = '_create'# bookmark_form.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')     # 클릭하면이동할 화면

    def get_initial(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return {'profile':profile}



class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['name','url']     # '__all__'
    template_name_suffix = '_update'    # bookmark_update.html
    # success_url 없으면 해당 model의 get_absolute_url() 호출
    # success_url = reverse_lazy('bookmark:list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')




    

