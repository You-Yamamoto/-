from django.urls import path
from app import views
from .views import readfunc

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('read/<int:pk>' , readfunc, name = 'read'),
]

