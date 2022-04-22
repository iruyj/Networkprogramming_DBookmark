from django.db import models

# Create your models here.
from django.shortcuts import resolve_url


class Bookmark(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()


    # 목록을 보여줄 때 object(1) 이렇게 보이는 게 아니라 이름으로 보여짐
    def __str__(self):
        return f'{self.name} : {self.url}'

    # 추가나 업데이트 시 성공url을 지정하지 않으면 이동할 디폴트 url
    def get_absolute_url(self):
        return resolve_url('bookmark:detail', pk=self.pk)