from django.urls import path
from . import views

urlpatterns = [
    path("", views.interest_view, name= 'interests-page')
]
