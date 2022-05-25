from django.urls import path
from .views import HomePage, ArticleDetailView, NewPost, UpdatePost, DeletePost

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('new_post/', NewPost.as_view(), name="new-post"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
]
