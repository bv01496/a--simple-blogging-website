from article.models import Catagory
def extra(request):
        cat = Catagory.objects.all()
        return {'catagories': cat}