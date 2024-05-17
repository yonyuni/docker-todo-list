from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # 할 일 목록을 보여줄 뷰 연결
    path('add/', views.todo_add, name='todo_add'), # 할 일을 추가할 뷰 연결
    path('edit/<int:pk>/', views.todo_edit, name='todo_edit'), # 할 일을 수정할 뷰 연결
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'), # 할 일을 삭제할 뷰 연결
] 