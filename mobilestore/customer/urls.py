from django.urls import path
from .views import *

urlpaterns = [
    path('cust/',CustHome.as_view(),name="custhome")
]