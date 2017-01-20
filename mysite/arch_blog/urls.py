from django.conf.urls import url
from . import views

app_name = 'arch_blog'
urlpatterns = [
    # ex /arch_blog/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex /arch_blog/4/
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name='post'),
    # ex /arch_blog/4/comment/
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name='comment')
] 