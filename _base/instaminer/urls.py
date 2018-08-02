from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('instamining/<str:query>/<int:instagram_id>/', views.query, name='query')
]
