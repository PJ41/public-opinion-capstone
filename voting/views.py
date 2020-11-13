from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


def dashboard(request):

    posts = Post.objects.order_by('-count')  # puts highest voted issue on top

    return render(request, 'voting/dashboard.html', {'posts': posts,})


def voteUp(request, post_name):
    posts = Post.objects.all()
    post = posts.get(header=post_name)
    post.count = post.count + 1
    post.save()

    return HttpResponseRedirect(reverse('dashboard', kwargs={}))

def voteDown(request, post_name=None):
    posts = Post.objects.all()
    post = posts.get(header=post_name)
    if post.count != 0:
        post.count = post.count - 1
    post.save()

    return HttpResponseRedirect(reverse('dashboard', kwargs={}))


class CreatePostView(generic.CreateView):
    model = Post
    fields = ['header', 'body']
    template_name = 'voting/createPost.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('dashboard', kwargs={}))



