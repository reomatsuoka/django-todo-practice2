from django.shortcuts import render
from django.views.generic import View
from .models import Todo

class IndexView(View):
  def get(self,request,*args,**kwargs):
    title = Todo.objects.order_by('deadline')

    return render(request,'app/index.html',{
      'todo_data': todo_data
    })
