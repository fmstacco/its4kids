from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Category, Post
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 9


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class ActivitiesView(generic.ListView):
    """
    Displays all activities posts in a page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 9


class AddPostView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    Logged users can add a post / activity to the blog
    """
    
    model = Post
    template_name = 'add_post.html'
    fields = 'title', 'category', 'featured_image', 'content', 

    def form_valid(self, form):
        if self.request.POST.get('status'):
            form.instance.status = int(self.request.POST.get('status'))
        form.instance.author = self.request.user
        messages.success(self.request, "Post added and waiting for approval")
        return super().form_valid(form)


class UpdatePostView(UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    """
    Logged users can update a post / activity they posted the blog
    """
    
    model = Post
    template_name = 'update_post.html'
    fields = 'title', 'category', 'featured_image', 'content',
    success_message = "Post updated successfully!"

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs.get('slug'))

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(self.request, "Post updated successfully")
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    """
    Logged users can delete a post / activity they posted in the blog
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')  # Redirect URL after successful deletion
    success_message = "Post deleted successfully!"

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    context = {'category': category, 'posts': posts}
    return render(request, 'category_posts.html', context)


