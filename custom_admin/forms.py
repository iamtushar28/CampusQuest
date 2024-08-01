from django import forms
from .models import QuestionPaper


#Question paper form
class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['paper_name', 'branch', 'year', 'pdf']
        widgets = {
            'paper_name': forms.TextInput(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }


#Login form
class CustomLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField() 