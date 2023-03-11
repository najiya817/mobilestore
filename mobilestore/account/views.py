from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .models import CustUser
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login
# Create your views here.


class RegView(CreateView):
    model=CustUser
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy("log")

class LogView(TemplateView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user.usertype == "customer":
                login(request,user)
                return redirect("custhome")
            elif user.usertype == "store":
                login(request,user)
                return redirect("storehome")
            

