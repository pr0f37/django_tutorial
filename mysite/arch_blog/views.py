from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Post, Comment

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_posts' : latest_posts
    }
    return render(request, 'arch_blog/index.html', context)
     
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
        HttpResponseRedirect(reverse('arch_blog:post', args=(post_id)))
    return HttpResponseRedirect(reverse('arch_blog:post', args=(post_id)))
    
        
