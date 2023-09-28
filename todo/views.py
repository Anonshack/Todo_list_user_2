from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .models import Todos


class TodoListView(ListView):
    template_name = 'todos/list.html'

    def get_queryset(self):
        try:
            fk = self.kwargs['fk']
            queryset = Todos.objects.filter(user=fk)
        except:
            queryset = Todos.objects.all()
        return queryset


class TodosCreateView(LoginRequiredMixin, CreateView):
    model = Todos
    template_name = 'todos/todos_new.html'
    fields = ('title', 'description', 'start_time', 'end_time', 'status')
    success_url = '/users/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Todos
    success_url = reverse_lazy('users')