from typing import Any
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class Blog_list_view(ListView):
    model=Articles
    template_name='blog/home.html'
    context_object_name='articles'
    ordering=['-date_posted']
    paginate_by=5

class UserBlog_list_view(ListView):
    model=Articles
    template_name='blog/user.html'
    context_object_name='articles'
    paginate_by=5

    def get_queryset(self) -> QuerySet[Any]:
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Articles.objects.order_by('-date_posted').filter(author=user)

class Blog_Detail_View(DetailView):
    model=Articles

class Blog_Create_View(LoginRequiredMixin,CreateView):
    model=Articles
    fields=['title','content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author=self.request.user
        return super().form_valid(form)
    
class Blog_Update_View(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Articles
    fields=['title','content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author=self.request.user
        return super().form_valid(form)


    def test_func(self) -> bool | None:
        post=self.get_object()

        if self.request.user==post.author:
            return True
        
        return False
    
class Blog_Delete_View(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Articles
    fields=['title','content']
    success_url='/'

    def test_func(self) -> bool | None:
        post=self.get_object()

        if self.request.user==post.author:
            return True
        
        return False

    
def about(requests):
    return render(requests,'blog/about.html')


