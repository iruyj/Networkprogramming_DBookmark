from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={ # 제한
        'pattern': '[a-z]+', # 정규표현식은 모두 대괄호에, + : 뒤에 더 이어질수있다.
        'title':'영어 소문자 대문자, 숫자만 가능, 특수문자, 공백입력안됨'
    }))
    nickname = forms.CharField(label='별명')

    class Meta(UserCreationForm):
        fields = UserCreationForm.Meta.fields + ('email',) # ('username', 'email',)

    def save(self):
        user = super().save() # user를 먼저 저장하기
        new_profile = Profile.objects.create(
            user=user,
            nickname=self.cleaned_data.get('nickname'), # self.cleaned_data['nickname']
        )
        return new_profile