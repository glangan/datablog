from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^all/$', views.posts_list),
    url(r'^tags/$', views.tags_list),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post_details),
    url(r'^tag/(?P<slug>[\w-]+)/$', views.tag_posts)
]
