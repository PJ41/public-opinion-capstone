from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


def dashboard(request):
    posts = Post.objects.all()

    return render(request, 'voting/dashboard.html', {'posts': posts, })


class CreatePostView(generic.CreateView):
    model = Post
    fields = ['header', 'body']
    template_name = 'voting/createPost.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('dashboard', kwargs={}))

