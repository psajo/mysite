from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('predict/', views.ci_bilstm)
]
