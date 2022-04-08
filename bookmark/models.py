from django.db import models

# Create your models here.
class Bookmark(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()


    # 목록을 보여줄 때 object(1) 이렇게 보이는 게 아니라 이름으로 보여짐
    def __str__(self):
        return f'{self.name} : {self.url}'