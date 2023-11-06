from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def picture(request):
    return render(request, "picture.html")

def advanced(requset):
    return render(requset, "advanced.html")
