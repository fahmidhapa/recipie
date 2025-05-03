from django.shortcuts import render,redirect
from . models import add_tbl
from django.contrib import messages
from django.conf import settings




# Create your views here.
def index(request):
    return render(request,"index.html")


def add(request):
    if request.method=='POST':
        title=request.POST.get('t')
        image=request.FILES.get('i')
        ingrediants=request.POST.get('ing')
        description=request.POST.get('d')
        instructions=request.POST.get('ins')
        obj=add_tbl.objects.create(title=title,image=image,ingrediants=ingrediants,description=description,instructions=instructions)
        obj.save()
        if obj:
            return render(request,"add.html",{"msg":"recipie uploaded" })
    return render(request,"add.html")

def view(request):
    obj=add_tbl.objects.all()
    return render(request,'allrecipes.html',{'data':obj})

def searchrecipie(request):
    rec= []
    if request.method == 'POST':
        ing = request.POST.get('ing', '').strip()
        if ing:
            rec = add_tbl.objects.filter(ingrediants__icontains=ing)
    return render(request, "search.html", {"rec": rec})
