from django.shortcuts import render

from post.models import Post

def posts(request): # receive request from a browser
    all_posts = Post.objects.all()  # Get all the objects of model or table 'Post'

    # It is view called by url --> context to render as an HTML template
    context = {
        'posts': all_posts
    }
    return render(request, 'posts.html', context) # context is the data
