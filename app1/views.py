from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'app1/index.html')
def login(request):
    return HttpResponse('<h1> Index page App1</h1>')

