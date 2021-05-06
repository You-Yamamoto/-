from django import forms

class PostForm(forms.Form):
    
    content = forms.CharField(max_length=140,  label='内容', widget=forms.Textarea())