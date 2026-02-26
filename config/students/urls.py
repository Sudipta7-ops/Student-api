from django.urls import path
from .views import StudentListCreate, StudentRetrieveUpdateDelete

urlpatterns = [
    path('students/', StudentListCreate.as_view()),
    path('students/<int:pk>/', StudentRetrieveUpdateDelete.as_view()),
]