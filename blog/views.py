from django.shortcuts import render

posts = [
    {
        'author': 'Gassdev',
        'title': 'Article du Blog 1',
        'content': 'Premier article du blog',
        'date_posted': '07 Janvier 2021',
        'image': 'http://placehold.it/300x300'
    },
    {
        'author': 'Jane Doe',
        'title': 'Article du Blog 2',
        'content': 'Deuxième article du blog',
        'date_posted': '08 Janvier 2021',
        'image': 'http://placehold.it/300x300'
    },
    {
        'author': 'John Doe',
        'title': 'Article du Blog 3',
        'content': 'Troisième article du blog',
        'date_posted': '09 Janvier 2021',
        'image': 'http://placehold.it/300x300'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})