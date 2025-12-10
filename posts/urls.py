from django.urls import path
from . import views
from .views import (
    PostCreateView,
    PostDeleteView,
    PostDraftListView,
    PostListView,
    PostArchivedListView,
    PostDetailView,
    PostUpdateView
)

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path("drafts/", PostDraftListView.as_view(), name="draft_list"),
    path("archived/", PostArchivedListView.as_view(), name="archived_list"),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('new/', views.PostCreateView.as_view(), name='new'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    ]