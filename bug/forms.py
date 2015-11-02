__author__ = 'chenpengpeng'
from .models import Event
from django import forms
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','content','business_type','version','platform','status',
                  'level','emergency','solution',
                  'reporter','channel', 'solution','attachment']
