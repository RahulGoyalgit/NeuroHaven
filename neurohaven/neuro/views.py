from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')

def upload(request):
    return render(request,'upload.html')

def result(request):
    return render(request,'result.html')

