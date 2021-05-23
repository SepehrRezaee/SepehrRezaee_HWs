from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('create/', views.create_post, name='create-post'),
]
