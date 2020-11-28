from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=30,default = 'uncatagorised')
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None,null=True,related_name='post-author+',blank=True)
    date_posted = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='post_image',default="default.jpg")
    like = models.ManyToManyField(User,related_name="likes")
    catagory = models.ManyToManyField(Catagory,related_name="cat")
    

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})
    def total_likes(self):
        return self.like.count()
        
class Comments(models.Model):
    comment = models.TextField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    # def get_absolute_url(self):
        # return reverse("article-detail", kwargs={"pk": self.pk})

    
    
    