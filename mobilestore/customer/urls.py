from django.urls import path
from .views import *

urlpatterns = [
    path('cust/',CustHome.as_view(),name="custhome")
]