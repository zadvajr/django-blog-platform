from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Daniel Zadva Jnr',
        'title': 'Getting Started with Django Framework',
        'content': 'This blog is about getting you started with Django 5.0. Please follow us for more information.',
        'date_posted': '21st May, 2024'
    },
    {
        'author': 'Jerry Ukke',
        'title': 'Web Development Fundamentals',
        'content': 'Welcome to web development fundamentals 101. You will be taught web dev in short time.',
        'date_posted': '21st May, 2024'
    }
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})