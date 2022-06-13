from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name="index"),
    path('page/<int:page>/', BlogView.as_view(), name="page"),
    path('<int:pk>/', PostDetail.as_view(), name="detail"),
    path('post/<int:pk>/', PostDetail.as_view(), name="post"), # detail
    path('category/<str:slug>/', category_page, name="category"),
path('tag/<str:slug>/', tag_page, name="tag"),
    path('create_post/', PostCreate.as_view(), name="create_post"),
    path('update_post/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name="delete_post"),
    path('<int:pk>/new_comment/', new_comment, name="new_comment"),
    path('update_comment/<int:pk>/', CommentUpdate.as_view(), name='update_commnet'),
    path('delete_comment/<int:pk>/', CommentDelete.as_view(), name="delete_comment"),
    #path('delete_comment/<int:pk>/', delete_comment, name="delete_comment"),
    path('search/<str:q>/', PostSearch.as_view(), name="search"),
]
