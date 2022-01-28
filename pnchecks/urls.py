from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileFieldFormView.as_view(), name='form-view'),
    path('result/', views.result, name="result"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

]
