from django.shortcuts import render

# Create your views here.

def ifblock(request):
    d={'a':10,'b':200,'c':30}
    return render(request,'ifblock.html',context=d)

def jinja_operations(request):
    return render(request,'jinja_operations.html',{'a':100,'b':70,'c':500})