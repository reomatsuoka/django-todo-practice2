from django.urls import path
from app import views

urlpatturns =[
  path('', views.IndexViews.as_view(), name='index')
]