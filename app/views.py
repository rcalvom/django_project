from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from app.models import File
from app.models import User
from app.forms import FileForm

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
            return redirect('/list_files')
    else:
        form = FileForm()
    context = {
        'form': form
    }
    return render(request, 'desktop.html', context)
