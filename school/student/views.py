from django.shortcuts import render
from .forms import StudForm,SForm
from .models import stud

# Create your views here.
def show(request):
    return render(request,"home.html")
def register(request):
    title="Student Registration"
    form = StudForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['s_name']
        name = form.cleaned_data['f_name']
        DOB = form.cleaned_data['s_DOB']
        clas = form.cleaned_data['s_class']
        address = form.cleaned_data['s_address']
        school = form.cleaned_data['s_school']
        email = form.cleaned_data['s_email']
        city = form.cleaned_data['s_city']
        state = form.cleaned_data['s_state']
        pin = form.cleaned_data['s_pin']

        p = stud(s_name=name,f_name=name,s_DOB=DOB,s_class=clas,s_address=address,s_school=school,s_email=email,s_city=city,s_state=state,s_pin=pin)
        p.save()
        return render(request,'ack.html',{"title":"Registered Successfully"})


    context={
    "title":title,
    "form":form,
    }
    return render(request,'register.html',context)
def existing(request):
    title="All Registered Students"
    queryset = stud.objects.all()
    context={
    "title":title,
    "queryset":queryset,
    }
    return render(request,'existing.html',context)
def search(request):
    title="Search Student"
    form=SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = stud.objects.filter(s_name=name)
        context={
            'title':title,
            'queryset':queryset,
        }
        return render(request,'existing.html',context)
    context={
    'title':title,
    'form':form,
    }
    return render(request,'search.html',context)

