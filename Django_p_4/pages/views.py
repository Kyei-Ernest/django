from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import (CreateView,
                                       UpdateView,
                                       DeleteView)
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'posts'  # optional [can use "<model>_list" as default in template]


class BlogDetailedView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_object(self):
        # customizing the primary key variable from default "pk" to "post_id"

        return Post.objects.get(id=self.kwargs['post_id'])  # noinspection PyUnresolvedReference


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")  # redirect after successfully processed
