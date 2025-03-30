from django.urls import path, include
from .views import dashboard
from . import views

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('password/change/', include('allauth.urls')),
]