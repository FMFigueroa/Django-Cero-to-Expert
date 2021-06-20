from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html') # luego de templates, colocar path que deseamos ver. 

def products(request):
    return render(request, 'app/products.html')

def projects(request):
    return render(request, 'app/projects.html')

def courses(request):
    return render(request, 'app/courses.html')

def blog(request):
    return render(request, 'app/blog.html')

def contacts(request):
    return render(request, 'app/contacts.html')