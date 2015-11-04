# coding=utf-8
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import EventForm
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


# Create your views here.
class AddEventView(FormView):
    # form = EventForm(request.POST or None)
    template_name='bug/addEvent.html'
    form_class = EventForm
    success_url = "/"
   # title = "提交问题"
    #context = {
    #    "title": title,
   #     "form": form,
   # }
    def form_valid(self,form):
        form.save(self.request.user)
        return super(AddEventView,self).form_valid(form)




def home(request):
    return render(request, "bug/dashboard.html", {})
