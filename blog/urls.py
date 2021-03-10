from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', views.post_list, name='post_list'),
    # ex: /blog/post/1/
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    # ex: /blog/post/new/
    path('post/new/', views.post_new, name='post_new'),
    # ex: /blog/post/1/edit/
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # ex: /blog/drafts/
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    # ex: /blog/post/1/publish/
    path('post/<pk>/publish', views.post_publish, name='post_publish'),
    # ex: /blog/post/1/remove/
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    # ex: /blog/post/1/comment/
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # ex: /blog/comment/1/approve/
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    # ex: /blog/comment/1/remove/
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

]