# coding=utf-8
from django.shortcuts import render
from .forms import EventForm
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Create your views here.
def addEvent(request):
    form = EventForm(request.POST or None)
    title="提交问题"
    context={
        "title":title,
        "form":form,
    }

    if form.is_valid():
        #instance = form.save(commit=False)
         form.save()


    return render(request, "bug/addEvent.html", context)

def home(request):
    return  render(request, "bug/dashboard.html",{})