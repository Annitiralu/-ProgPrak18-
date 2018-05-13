from django import forms

from .models import Task


class PostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_text', 'deadline')


class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_text', 'deadline', 'progress', 'done')