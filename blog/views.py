from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'Anurag',
        'title':'Blog Post 1',
        'content': 'first post content dummy content',
        'date_posted':'sept 23, 2023'
    },
    {   
        'author':'kamboj',
        'title':'Blog Post 2',
        'content': 'first post content dummy content',
        'date_posted':'sept 23, 2023'
    },
    {
        'author':'Sandha',
        'title':'Blog Post 3',
        'content': 'first post content dummy content',
        'date_posted':'sept 23, 2023'
    },
    {
        'author':'Kamboj',
        'title':'Blog Post 4',
        'content': 'first post content dummy content',
        'date_posted':'sept 23, 2023'
    },
]

def Home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
