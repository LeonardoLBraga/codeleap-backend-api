from django.urls import path
from .views import PostListCreateAPIView, PostUpdateDeleteAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view()),
    path('<int:pk>/', PostUpdateDeleteAPIView.as_view()),
]
