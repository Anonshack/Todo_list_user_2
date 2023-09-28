from django.urls import path
from .views import TodoListView, TodosCreateView, PostDeleteView


urlpatterns = [
    path('todos/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('list/<int:fk>/', TodoListView.as_view(), name='todo_list'),
    path('todos/new/', TodosCreateView.as_view(), name='todo_new'),
]