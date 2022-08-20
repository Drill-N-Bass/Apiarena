from django.urls import path
from . import views

urlpatterns = [
    path('pawel_pedryc_developer/', views.home_view_pawel)
]