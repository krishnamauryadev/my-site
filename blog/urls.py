from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('posts', views.posts, name='posts_page'),
    path('post-detail/<slug:slug>', views.post_detail, name='post_detail')
]
