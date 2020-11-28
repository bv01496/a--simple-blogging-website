from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileDetail,UpdateProfile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('signup', views.register,name = "signup"),
    path ('login', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path ('logout',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path ('profile/<int:pk>',ProfileDetail.as_view(),name='profile'),
    path ('update/<int:pk>',UpdateProfile.as_view(),name='update'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)