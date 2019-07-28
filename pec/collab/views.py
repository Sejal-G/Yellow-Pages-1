from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Server
from .forms import cform,pform,mform,dform,userform,filterform,eform,clform,coform,nform
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Carpenter
from .models import Plumber
from .models import Mason,Driver,Cook,Cleaner,Electrician,Nurse
import requests
import math
from math import radians, cos, sin, asin, sqrt

def home(request):
    return render(request,'home.html',{ })

def csignup(request):
    form=cform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        messages.success(request,"SUCCESSFULLY SIGNED UP")
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        try:
            response = requests.get(url, params=data)
            geoArray = response.json()
            print (geoArray)
            instance.lat=geoArray[0]["lat"]
            instance.long=geoArray[0]["lon"]
            print(instance.lat)
            print(instance.long)
        except:
            print("in except")
        instance.save()
        # messages.success(request,"SUCCESSFULLY SIGNED UP")
    # else:
    #     messages.error(request,"error")
    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,
    }
    return render(request,'cform.html',context)

def esignup(request):
    form=eform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        messages.success(request,"SUCCESSFULLY SIGNED UP")
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        try:
            response = requests.get(url, params=data)
            geoArray = response.json()
            print (geoArray)
            instance.lat=geoArray[0]["lat"]
            instance.long=geoArray[0]["lon"]
            print(instance.lat)
            print(instance.long)
        except:
            print("in except")
        instance.save()
        # messages.success(request,"SUCCESSFULLY SIGNED UP")
    # else:
    #     messages.error(request,"error")
    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,
    }
    return render(request,'cform.html',context)

def cosignup(request):
    form=coform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        messages.success(request,"SUCCESSFULLY SIGNED UP")
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        try:
            response = requests.get(url, params=data)
            geoArray = response.json()
            print (geoArray)
            instance.lat=geoArray[0]["lat"]
            instance.long=geoArray[0]["lon"]
            print(instance.lat)
            print(instance.long)
        except:
            print("in except")
        instance.save()
        # messages.success(request,"SUCCESSFULLY SIGNED UP")
    # else:
    #     messages.error(request,"error")
    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,
    }
    return render(request,'cform.html',context)

def clsignup(request):
    form=clform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        messages.success(request,"SUCCESSFULLY SIGNED UP")
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        try:
            response = requests.get(url, params=data)
            geoArray = response.json()
            print (geoArray)
            instance.lat=geoArray[0]["lat"]
            instance.long=geoArray[0]["lon"]
            print(instance.lat)
            print(instance.long)
        except:
            print("in except")
        instance.save()
        # messages.success(request,"SUCCESSFULLY SIGNED UP")
    # else:
    #     messages.error(request,"error")
    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,
    }
    return render(request,'cform.html',context)

def nsignup(request):
    form=nform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        messages.success(request,"SUCCESSFULLY SIGNED UP")
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        try:
            response = requests.get(url, params=data)
            geoArray = response.json()
            print (geoArray)
            instance.lat=geoArray[0]["lat"]
            instance.long=geoArray[0]["lon"]
            print(instance.lat)
            print(instance.long)
        except:
            print("in except")
        instance.save()
        # messages.success(request,"SUCCESSFULLY SIGNED UP")
    # else:
    #     messages.error(request,"error")
    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,
    }
    return render(request,'cform.html',context)

def psignup(request):
    form=pform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        # messages.success(request,"SUCCESSFULLY SIGNED UP")
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        try:
            response = requests.get(url, params=data)
            geoArray = response.json()
            print (geoArray)
            instance.lat=geoArray[0]["lat"]
            instance.long=geoArray[0]["lon"]
            print(instance.lat)
            print(instance.long)
        except:
            print("in except")
        instance.save()
        messages.success(request,"SUCCESSFULLY SIGNED UP")
    # else:
    #     messages.error(request,"error")
    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,
    }
    return render(request,'cform.html',context)

def msignup(request):
    form=mform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        try:
            print("hello")
            response = requests.get(url, params=data)
            geoArray = response.json()
            print (geoArray)
            instance.lat=geoArray[0]["lat"]
            instance.long=geoArray[0]["lon"]
            print(instance.lat)
            print(instance.long)
            print("still there")
        except:
            print("in except")
        instance.save()
        messages.success(request,"SUCCESSFULLY SIGNED UP")
    # else:
    #     messages.error(request,"error")
    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,
    }
    return render(request,'cform.html',context)

def dsignup(request):
    form=dform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        # messages.success(request,"SUCCESSFULLY SIGNED UP")
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"

        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        try:
            print("hello")
            response = requests.get(url, params=data)
            geoArray = response.json()
            print (geoArray)
            instance.lat=geoArray[0]["lat"]
            instance.long=geoArray[0]["lon"]
            print(instance.lat)
            print(instance.long)
            print("still there")
        except:
            print("in except")
        instance.save()
        messages.success(request,"SUCCESSFULLY SIGNED UP")

    # else:
    #     messages.error(request,"error")
    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,
    }
    return render(request,'cform.html',context)

def server_create(request):
    return HttpResponse("<h1>create</h1>")

def server_update(request):
    return HttpResponse("<h1>update</h1>")
def server_delete(request):
    return HttpResponse("<h1>delete</h1>")


def server_list(request):

    queryset_list=Server.objects.all()
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(profession=query)

    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    # return render(request, 'service.html', {'object_list': queryset})
    context = {
    "object_list":queryset,

    }
    return render(request,'services.html',context)

def Carpenter_list(request):
    queryset_list=Carpenter.objects.all()
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(name=query)
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    context = {
    "object_list":queryset,
    }
    return render(request,'list.html',context)

def Electrician_list(request):
    queryset_list=Electrician.objects.all()
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(name=query)
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    context = {
    "object_list":queryset,
    }
    return render(request,'list.html',context)

def Cook_list(request):
    queryset_list=Cook.objects.all()
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(name=query)
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    context = {
    "object_list":queryset,
    }
    return render(request,'list.html',context)

def Cleaner_list(request):
    queryset_list=Cleaner.objects.all()
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(name=query)
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    context = {
    "object_list":queryset,
    }
    return render(request,'list.html',context)

def Nurse_list(request):
    queryset_list=Nurse.objects.all()
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(name=query)
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    context = {
    "object_list":queryset,
    }
    return render(request,'list.html',context)

def Plumber_list(request):
    queryset_list=Plumber.objects.all()
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(profession=query)
    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    # return render(request, 'service.html', {'object_list': queryset})
    context = {
    "object_list":queryset,
    }
    return render(request,'list.html',context)

def Mason_list(request):
    queryset_list=Mason.objects.all()
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(profession=query)
    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    # return render(request, 'service.html', {'object_list': queryset})
    context = {
    "object_list":queryset,
    }
    return render(request,'list.html',context)

def Driver_list(request):
    queryset_list=Driver.objects.all()
    paginator = Paginator(queryset_list, 3,orphans=1) # Show 25 contacts per page
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(profession=query)
    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    # return render(request, 'service.html', {'object_list': queryset})
    context = {
    "object_list":queryset,
    }
    return render(request,'list.html',context)

def Carpenter_detail(request,id):
    instance=get_object_or_404(Post,id=id)
    storage=messages.get_messages(request)
    context={
    "title":instance.title,
    "instance":instance,
    "messages":storage,
    }
    return render(request,'post_details.html',context)

def pdelete(request,id):
        instance=get_object_or_404(Question,id=id)
        instance.delete()

        return redirect('plist')

def user(request):
    form=userform(request.POST or None,request.FILES or None)
    ser=(request.POST.get("service"))
    print("ser",ser)

    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()
        messages.success(request,"LOCATION ENTERED")
        address=form.cleaned_data.get('address')
        print(address)
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
        'key': '3319b0b5566c86',
        'q': address,
        'format': 'json'
        }
        print("hello")
        response = requests.get(url, params=data)
        geoArray = response.json()
        print (geoArray)
        instance.lat=geoArray[0]["lat"]
        instance.long=geoArray[0]["lon"]
        global l2
        if ser=="Carpenter":
            l2=Carpenter.objects.values()
        elif ser=="Plumber":
            l2=Plumber.objects.values()
        elif ser=="Mason":
            l2=Mason.objects.values()
        elif ser=="Driver":
            l2=Driver.objects.values()
        elif ser=="Cook":
            l2=Cook.objects.values()
        elif ser=="Cleaner":
            l2=Cleaner.objects.values()
        elif ser=="Electrician":
            l2=Electrician.objects.values()
        elif ser=="Nurse":
            l2=Nurse.objects.values()
        else:
            l2=[]
        print(l2)

        print(l2[0]["name"])
        lat1=float(instance.lat)
        lon1 =float(instance.long)
        print(lat1,lon1)
        for i in l2:
            lat2,lon2 =i['lat'],i['long']
            print(lat2)
            print(lon2)
            radius = 6378 # km
            print("dist calculation")
            print("yes")

            dlat =math.radians(lat2-lat1)

            dlon = math.radians(lon2-lon1)
            print("still there")
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = radius * c
            print("dist is",d)
            global t
            if ser=="Carpenter":
                t=Carpenter.objects.get(id=i['id'])
            elif ser=="Plumber":
                t=Plumber.objects.get(id=i['id'])
            elif ser=="Driver":
                t=Driver.objects.get(id=i['id'])
            elif ser=="Mason":
                t=Mason.objects.get(id=i['id'])
            elif ser=="Cook":
                t=Cook.objects.get(id=i['id'])
            elif ser=="Cleaner":
                t=Cleaner.objects.get(id=i['id'])
            elif ser=="Electrician":
                t=Electrician.objects.get(id=i['id'])
            elif ser=="Nurse":
                t=Nurse.objects.get(id=i['id'])

            # b print(t)
            t.dist=d
            t.save()
        if ser=="Carpenter":
            return HttpResponseRedirect('clist')
        elif ser=="Plumber":
            return HttpResponseRedirect('plist')
        elif ser=="Driver":
            return HttpResponseRedirect('dlist')
        elif ser=="Mason":
            return HttpResponseRedirect('mlist')
        elif ser=="Cook":
            return HttpResponseRedirect('colist')
        elif ser=="Cleaner":
            return HttpResponseRedirect('cllist')
        elif ser=="Electrician":
            return HttpResponseRedirect('elist')
        elif ser=="Nurse":
            return HttpResponseRedirect('nlist')
        else:
            print("invalid")

        instance.save()

    # else:
    #     messages.error(request,"Error")

    data = request.POST.copy()
    loc=data.get('address')
    print(loc)
    context={
        "form":form,
        "loc":loc,

    }
    return render(request,'userform.html',context)

def filter(request):
        form=filterform(request.POST or None,request.FILES or None)
        ser=(request.POST.get("service"))
        print(ser)
        if form.is_valid():
            instance = form.save(commit=False)
            # instance.save()
            messages.success(request,"SUCCESSFULLY SIGNED UP")
            instance.save()
            messages.success(request,"SUCCESSFULLY SIGNED UP")

        else:
            messages.error(request,"error")

        context={
            "form":form,

        }
        return render(request,'filter.html',context)
