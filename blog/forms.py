from django import forms
from tinymce.widgets import TinyMCE
from .models import *

class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()

    content = forms.CharField(widget=TinyMCE(attrs={'cols':40, 'rows': 20}))

    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['category'].widget.attrs.update({'class': 'form-control'})