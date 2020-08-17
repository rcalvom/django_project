from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from app.models import File
from app.models import User
from app.forms import FileForm

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

def list_files(request):
    files = File.objects.all()
    context = {
        'files': files
    }
    return render(request, 'desktop.html', context)

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/desktop')
    else:
        form = FileForm()
    context = {
        'form': form
    }
    return render(request, 'desktop.html', context)
