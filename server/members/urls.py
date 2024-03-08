from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('predict', views.predict, name='predict')
]