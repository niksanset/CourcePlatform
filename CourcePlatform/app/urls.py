from django.urls import path
from app.views import *


urlpatterns = [
    path('', course_list_view, name='course_list'),
    path('course_create/<int:pk>/', course_create_view, name='course_create'),
    path('course_update/<int:pk>/', course_update_view, name='course_update'),
    path('course_delete/<int:pk>/', course_delete_view, name='course_delete'),
    path('course_detail_module_list/',course_detail_module_list_view, name='course_detail_model_list'),
    path('module_create/<int:pk>/',module_create_view, name='module_create'),
    path('module_update/<int:pk>/',module_update_view, name='module_update'),
    path('module_delete/<int:pk>/',module_delete_view, name='module_delete'),
    path('module_detail_lesson_list/',module_detail_lesson_list_view, name='module_detail_lesson_list'),
    path('lesson_create/<int:pk>/',lesson_create_view, name='lesson_create'),
    path('lesson_delete/<int:pk>/',lesson_delete_view, name='lesson_delete'),
    path('lesson_update/<int:pk>/',lesson_update_view, name='lesson_update'),
    path('lesson_detail/',lesson_detail_view, name='lesson_detail'),
]
