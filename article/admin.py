from django.contrib import admin
from .models import Article,Catagory,Comments
# Register your models here.
admin.site.register(Article)
admin.site.register(Catagory)
admin.site.register(Comments)
