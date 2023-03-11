from django.urls import path
from .views import RegView

urlpatterns = [
    path('reg',RegView.as_view(),name="reg"),
]