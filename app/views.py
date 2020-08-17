
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from app.models import File, User
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

def upload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = upload_file.name
        path = fs.save(upload_file.name, upload_file)
        path = fs.url(path)
        context['url'] = path
        file = File(name=name, path=path)
        file.save()
    return render(request, 'upload.html', context)
