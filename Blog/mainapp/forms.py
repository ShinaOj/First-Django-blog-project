from django import forms
from .models import Author, Category, Tag, Post, Comment

class Tagform(forms.Form):
    name=forms.CharField(max_length=100, min_length=6)
    

class AuthForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=["name"]

class PostForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'h-full-width'}))
    tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget= forms.SelectMultiple(attrs={'class':'h-full-width'}))
    class Meta:
        model=Post
        fields=['title', 'article', 'category', 'tags']
        widgets={
            'title': forms.TextInput(attrs={'class': 'h-full-width'}),
            'article':forms.Textarea(attrs={'class': 'h-full-width'}),
             }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name', 'email', 'comment']
        widgets={
            'name': forms.TextInput(attrs={'class': 'h-full-width', 'placeholder': 'your names'}),
            'email': forms.EmailInput(attrs={'class': 'h-full-width', 'placeholder': 'your email'}),
            'comment': forms.Textarea(attrs={'class': 'h-full-width', 'placeholder': 'your comment'})
        }