from django.shortcuts import render

# Create your views here.

def data_render(request):
    d = {'name':'Rohan','age':24}
    return render(request,'data_render.html',context=d)