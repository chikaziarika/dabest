from django import forms
from .models import *
from django_ckeditor_5.widgets import CKEditor5Widget

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control Author",'disabled':'disabled'}
        ),
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )


class BlogForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'image', 'textarea', 'author', 'tags']
        widget = {
            'textarea':CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="comment"
              )
        }
        labels = {
            'textarea': 'Konten',
            'headline': 'Judul Artikel',
            'Image': 'Gambarl',
            'author':'Author',
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['headline'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['image'].widget.attrs.update({'class': 'form-control' })
        self.fields['textarea'].required = False
        self.fields['author'].widget.attrs.update({'class': 'form-control' })
        self.fields['tags'].widget.attrs.update({'class': 'form-select tags', 'style':'text-align:center; width:15%' })