from django.shortcuts import render
from app.models import User

def login_view(request):
    if request.GET:
        username = request.GET["user"]
        password = request.GET["password"]
        user = User.objects.get(username=username)
        if user:
            if password  == user.password:
                request.GET = None
                return render(request, 'desktop.html', {})
            else:
                return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


def desktop_view(request):
    return render(request, 'desktop.html', {})