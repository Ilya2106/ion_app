from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("new/", views.PostCreateView.as_view(), name="post_new"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("<int:comment_id>/comment/", views.add_comment, name="add_comment"),
    path("<int:like_id>/like/", views.add_like, name="add_like"),
]
