from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'app2/index.html')
def login(request):
    return HttpResponse('<h1> Index page App2</h1>')
