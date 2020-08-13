from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html', {})

def desktop_view(request):
    return render_to_response(request, 'desktop.html', {})