from django.shortcuts import render, redirect
from app.models import User
from django.http import HttpResponseRedirect

def login_view(request):
        if request.method == "POST":
            try:
                user = User.objects.get(username=request.POST["username"])
                if user.password == request.POST["password"]:               
                    return redirect(desktop_view)
                else:
                    return render(request, 'login.html', {"user_correct": True, "pass_correct": False})
            except:
                return render(request, 'login.html', {"user_correct": False, "pass_correct": True})
        else:
            return render(request, 'login.html', {"user_correct": True, "pass_correct": True})


def desktop_view(request):
    return render(request, 'desktop.html', {})