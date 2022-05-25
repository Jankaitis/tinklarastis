from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy

class HomePage(ListView):
    model = BlogPost
    paginate_by = 2
    template_name = 'home.html'
    ordering = ['-date_added']

class ArticleDetailView(DetailView):
    model = BlogPost
    template_name = 'article_details.html'

class NewPost(CreateView):
    model = BlogPost
    template_name = 'new_post.html'
    fields = '__all__'

class UpdatePost(UpdateView):
    model = BlogPost
    template_name = 'update_post.html'
    fields = ['title', 'body']

class DeletePost(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')