from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Articlelist.as_view(), name="home"),
    path('detail/<int:pk>',views.ArticleDetail.as_view(),name='article-detail'),
    path('like',views.liked ,name='article-like'),
    path('create',views.Create_post.as_view() ,name='article-create'),
    path('catagory/<id>',views.catagory_list,name='catagory'),
    path('liked',views.liked_post,name='liked-article'),
    path('comment',views.comments,name='article-comment'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
