# from django import forms
# from .models import Comment


# class CommentForm(forms.ModelForm):
#     # captcha = ReCaptchaField()

#     class Meta:
#         model = Comment
#         fields = ("text",)  # + "captcha"
#         # widgets = {
#         #     "text": forms.Textarea(attrs={"class": "form-control border"}),
#         # }

from django.forms import ModelForm
from .models import Comment, Like


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ["value"]
