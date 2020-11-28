from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "outsider blog admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('article.urls')),
    path('',include('user.urls')),
]
