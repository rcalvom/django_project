from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from app.models import File

def login_view(request):
    return render(request, 'login.html', {})

def desktop_view(request):
    return render_to_response(request, 'desktop.html', {})

def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = upload_file.name
        path = fs.save(upload_file.name, upload_file)
        path = fs.url(path)
        file = File(name=name, path=path)
        file.save()
    return render(request, 'upload.html', {})
