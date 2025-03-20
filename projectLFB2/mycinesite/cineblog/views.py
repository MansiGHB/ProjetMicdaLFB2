from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-updated_on')
    template_name = 'accueil.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'pagepost.html'
