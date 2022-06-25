from audioop import reverse
from django.shortcuts import render
from django.views import generic


class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model = Post

class PostUPdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(generic.UpdateView):
    model = PostCreateView
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
