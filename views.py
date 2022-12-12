from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, LikeForm

# from django.core.exceptions import ObjectDoesNotExist
from .models import Post
from .permissions import AuthorPermissionsMixin

# from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "ion/post_list.html"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "ion/post_detail.html"


class PostUpdateView(AuthorPermissionsMixin, UpdateView):
    model = Post
    fields = [
        "text",
    ]
    template_name = "ion/post_edit.html"


class PostDeleteView(AuthorPermissionsMixin, DeleteView):
    model = Post
    template_name = "ion/post_delete.html"
    success_url = reverse_lazy("post_list")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "ion/post_new.html"
    fields = [
        "text",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# def home(request):
#     if request.method == "POST":
#         id = request.POST.get("id", None)
#         if id:
#             try:
#                 post = Post.objects.get(pk=id)
#             except ObjectDoesNotExist:
#                 return ()  # обработка ошибки пост не найден
#             if form.is_valid():
#                 form = form.save(commit=False)
#                 form.author = request.author
#                 form.post = post
#                 form.save()
#                 return ()  # все хорошо, коммент сохранен
#             return ()  # обработка ошибки форма не валидная
#         return ()  # обработка ошибки id не передан
#     # else здесь не обязательно писать код выполнится только если не ПОСТ
#     context = {
#         "form": CommentForm(),
#         "comments": Comment.objects.filter(moderation=True),
#     }
#     return (request, "ion/post_detail.html", context)  # return метод GET


@login_required(login_url="login")
def add_comment(request, comment_id):
    form = CommentForm()
    post = get_object_or_404(Post, id=comment_id)
    author = request.user

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = author
            comment.post = post
            comment.save()
            return redirect("post_detail", post.id)

    context = {"form": form, "post": post}

    return render(request, "ion/comment_form.html", context)


# @login_required(login_url="login")
# def add_like(request, like_id):
#     form = LikeForm
#     post = get_object_or_404(Post, pk=like_id)
#     author = request.user

#     if request.method == "POST":
#         form = LikeForm(request.POST)
#         if form.is_valid():
#             if form.Meta.fields["value"] == 1:
#                 like = form.save(commit=False)
#                 like.author = author
#                 like.post = post
#                 like.save()
#                 return redirect("post_detail", post.id)
#             elif form.Meta.fields["value"] == -1:
#                 dislike = form.save(commit=False)
#                 dislike.author = author
#                 dislike.post = post
#                 dislike.save()
#                 return redirect("post_detail", post.id)

#     context = {"form": form, "post": post}

#     return render(request, "ion/like_form.html", context)


@login_required(login_url="login")
def add_like(request, like_id):
    form = LikeForm
    post = get_object_or_404(Post, pk=like_id)
    author = request.user

    if request.method == "POST":
        form = LikeForm(request.POST)
        if form.is_valid():
            like = form.save(commit=False)
            like.author = author
            like.post = post
            like.save()
            return redirect("post_detail", post.id)

    context = {"form": form, "post": post}

    return render(request, "ion/like_form.html", context)
