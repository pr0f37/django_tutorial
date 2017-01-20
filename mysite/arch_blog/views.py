from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Post, Comment


class IndexView(generic.ListView):
    template_name = 'arch_blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]
     
def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.getComments()
    tags = post.getTags()
    return render(request, 'arch_blog/post.html', {'post' : post, 'comments': comments, 'tags': tags,})

def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:              
        c = Comment()
        c.body = request.POST['body']
        c.author = request.POST['author']
        c.pub_date = timezone.now()
        c.post = post
        c.save()
    except:
        HttpResponseRedirect(reverse('arch_blog:index'))
    return HttpResponseRedirect(reverse('arch_blog:post', args=(post_id)))
    
        
