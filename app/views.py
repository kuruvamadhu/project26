from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

def fbv_string(request):
    return HttpResponse('<h1> this is fbv page </h1>')

class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1>This is CBV string</h1>')

class Cbv_first(View):
    def get(self,request):
        return render(request,'Cbv_first.html')
