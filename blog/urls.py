from . import views
from django.urls import path
from .views import ActivitiesView, AddPostView

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('blog/', ActivitiesView.as_view(), name='blog'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]