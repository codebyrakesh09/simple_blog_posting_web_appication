from django import forms
from .models import Post, Contact

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title of your post'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here', 'rows': 6}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name here'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email here'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message  here','rows': 4}),
        }


