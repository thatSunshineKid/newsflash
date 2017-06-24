from django.conf.urls import url
from django.contrib import admin
from .views import index, PostListView, PostDetailView, PostCreate, AuthorCreate


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create/$', PostCreate.as_view(), name="PostCreate"),
    url(r'^write/$', AuthorCreate.as_view(), name="AuthorCreate"),
    url(r'^posts/$', PostListView.as_view(), name='posts'),
    url(r'^post/(?P<pk>\d+)$', PostDetailView.as_view(), name='post-detail'),


]
