from django.urls import path
from .views import BookAPIView, BookAPIViewDetail

urlpatterns = [
    path('', BookAPIView.as_view(), name='book_list'),
    path('<int:pk>/', BookAPIViewDetail.as_view(), name='book_detail'),
]