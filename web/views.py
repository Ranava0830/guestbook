from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# 留言列表
class MessageList(ListView):
    model = Message

class MessageDetail(LoginRequiredMixin ,DetailView):
        model = Message


class MessageCreate(CreateView):
     model = Message
     field = ['user','subject','content']
     success_url = reverse_lazy('msg_list')
     
class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('msg_delete')
















    