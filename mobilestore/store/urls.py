from django.urls import  path

from .views import *

urlpatterns = [
    path('cust/',StoreHome.as_view(),name="storehome")
]