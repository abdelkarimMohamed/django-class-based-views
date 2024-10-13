from django.shortcuts import render,get_list_or_404
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

class PostList(ListView):
    model = Post
    # context_object_name = 'all_posts'
    ordering = ['-created_at']
    # queryset = Post.objects.filter(active=True)	
    # template_name = 'post/test.html'	
    def get_queryset(self):
        return Post.objects.filter(active=True)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['myname']='karim'
        return context

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post

class PostDelete(DeleteView):
    model = Post

class PostUpdate(UpdateView):
    model = Post


