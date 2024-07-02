from django.urls import path
from . import views

urlpatterns = [
    path('', views.gym_classes_list, name='gym_classes_list'),
    path('book/<int:class_id>/', views.book_gym_class, name='book_gym_class'),
]