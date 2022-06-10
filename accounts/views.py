from django.shortcuts import render

# Create your views here.
from accounts.forms import RegisterForm


def register(request):
    if request.method == 'POST': # 정보를 입력하고
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return render(request, 'account/templates/accounts/register_done.html', {'profile':profile})
    else:                        # 처음 빈 폼 화면
        form = RegisterForm()
        return render(request, 'accounts/register.html',{'form':form})