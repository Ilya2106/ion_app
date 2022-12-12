from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images/", blank=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    class Meta:
        ordering = ["-date"]

    def likes_count(self):
        return Like.objects.filter(value__value="лайк").count()

    def dislikes_count(self):
        return Like.objects.filter(value__value="дизлайк").count()


class Comment(models.Model):
    text = models.TextField(max_length=5000)
    date = models.DateTimeField(default=timezone.now, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE, null=True
    )
    image = models.ImageField(upload_to="comment_images/", blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-date"]


class Grade(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        ordering = ["-value"]


class Like(models.Model):
    value = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.value} - {self.author} - {self.post}"


# class Comment(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     text = models.TextField(max_length=5000)
#     parent = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=timezone.now, null=True)
#     moderation = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.text} - {self.post}"
