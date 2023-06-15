from . import views
from django.urls import path
from .views import ActivitiesView

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('blog/', ActivitiesView.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

]