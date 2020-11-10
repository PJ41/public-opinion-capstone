from django.shortcuts import render
from .models import *


def dashboard(request):
    posts = Post.objects.all()

    return render(request, 'voting/dashboard.html', {'posts': posts, })

