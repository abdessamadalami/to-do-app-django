from django import forms
from django.forms import ModelForm
from .models import *



class TasksForm(forms.ModelForm):
      class Meta:
          model = Tasks
          fields = '__all__'
