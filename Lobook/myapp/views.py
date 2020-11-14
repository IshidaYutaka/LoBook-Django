from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html', {})

def register(request):
    return render(request, 'myapp/register/register.html', {})

def list(request):
    return render(request, 'myapp/list.html', {})