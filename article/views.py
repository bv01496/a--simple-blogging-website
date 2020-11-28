from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DeleteView,UpdateView,DetailView,CreateView
from .models import Article,Catagory,Comments
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
class Articlelist(ListView):
    model = Article
    template_name = 'article/home.html'
    context_object_name = 'posts'
    paginate_by = 4
class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Article,id= self.kwargs['pk'])
        total_likes = stuff.total_likes()

        if stuff.like.filter(id=self.request.user.id).exists():
            is_liked = True
        else:
            is_liked = False
        commen = Comments.objects.filter(article= stuff)
        
        context["comments"] = commen
        context["total_likes"] = total_likes
        context["is_liked"] = is_liked
        return context

def liked(request):
    if request.method == 'POST':
        postid = request.POST.get('idr')
        print(postid)                                                                                                                                                                                        
        post = Article.objects.get(id= postid)
        if post.like.filter(id = request.user.id).exists():
            post.like.remove(request.user)
            post.save()
            return JsonResponse({'status':'like'})
        else:
            post.like.add(request.user)
            post.save()
            return JsonResponse({'status':'liked'})
    else:
        return HttpResponse('404 not found')


def catagory_list(request,id):
    cat_list = Article.objects.filter(catagory= id)
    cat = Catagory.objects.get(id=id)
    p = Paginator(cat_list,2)
    
    return render(request,'article/article_list.html',{'posts': cat_list,'cat':cat,'page_obj':p})

class Create_post(CreateView,LoginRequiredMixin):
    model = Article
    fields = ('title','content','image','catagory')
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
def liked_post(request):
    posts = Article.objects.all()
    liked = []
    for post in posts:
        if post.like.filter(id=request.user.id).exists():
            liked.append(post)
    return render(request,'article/article_liked.html',{'posts':liked})

def comments(request):
    if request.method == 'POST':
        com = request.POST.get('comment')
        post_id = request.POST.get('post_id')
        art = Article.objects.get(id= post_id)
        Comments.objects.create(comment=com,user=request.user,article= art)
        return JsonResponse({'status':'commented'})
    else:
        return HttpResponse('404 forbidden')