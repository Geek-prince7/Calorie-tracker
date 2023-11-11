from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    if request.method=='POST':
        food=Food.objects.get(name=request.POST.get('food',''))
        user=request.user
        Consume(user=user,food_consumed=food).save()
    foods=Food.objects.all()
    consumed_foods=Consume.objects.filter(user=request.user)
    return render(request,'tracker/index.html',{'foods':foods,'consumed_foods':consumed_foods})


def delete_consumed(request,id):
    consumed=Consume.objects.get(id=id)
    if request.method=='POST':
        consumed.delete()
        return redirect('/')
    return render(request,'tracker/delete.html',{})