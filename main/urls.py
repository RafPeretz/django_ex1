from django.urls import path
from . import views

urlpatterns = [
    path ('homepage/',views.homepage),
    path('about/',views.about),
    path('today/',views.today)
]
