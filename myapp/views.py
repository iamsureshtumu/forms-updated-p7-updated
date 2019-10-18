from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
# Create your views here.

def page1(request):
    return HttpResponse("<h1>welcome to page 1</h1>")

def page2(request):
    return render(request,'page2.html',context={'data':"data is passed"})

def topic(request):
    d={'objects':Topic.objects.all()}
    return render(request,'page3.html',context=d)

def records(request):
    d={'objects':Access_Records.objects.order_by('date')}
    return render(request,'page4.html',context=d)

def page5(request):
    data=Topic.objects.all()
    return render(request,'page8.html',context={'objects':data})

def display(request):
    print(request.POST)
    #print(request.POST['topic'])
    topics=Topic.objects.all()
    qs=Webpage.objects.none()
    for top in topics:       
        if top.topic in request.POST:
            data=request.POST.get(top.topic,"Key not found")
            qs=qs.union(Webpage.objects.all().filter(topic=data))
    return render(request,'page6.html',context={'objects':qs})









