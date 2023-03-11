from django.urls import  path

from .views import *

urlpaterns = [
    path('cust/',StoreHome.as_view(),name="storehome")
]