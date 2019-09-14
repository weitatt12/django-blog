from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CorneyMS',
        'title': 'Blog Post 1',
        'content': 'First post conetnt',
        'date_posted': 'Aug 27, 2018'
    },
    {
        'author': 'Johnny',
        'title': 'Blog Post 2',
        'content': 'Second post conetnt',
        'date_posted': 'Aug 28, 2017'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
