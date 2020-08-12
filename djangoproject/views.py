from django.http import HttpResponse

def hello_world(request):
    nombre = "Ricardo"
    return HttpResponse("<html><body><h3>{}</h3></body></html>".format(nombre))