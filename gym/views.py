from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from . models import *

###############///////////////---------------C-R-E-A-T-I-N-G     H-O-M-E     PAGE VIEWS---------------\\\\\\\\\\\\\\\###############


def home(request):
    return render(request, 'gym/home.html')


def about(request):
    return render(request, 'gym/about.html')


def contact(request):
    return render(request, 'gym/contact.html')


def services(request):
    return render(request, 'gym/services.html')



def signin(request):
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        try:
            if user.is_authenticated:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'gym/signin.html', context)


def signout(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    logout(request)
    return redirect('signin')

###############///////////////---------------CREATING ENQUIRY VIEWS---------------\\\\\\\\\\\\\\\###############


def add_enq(request):
    error = ""
    if request.method == "POST":
        n = request.POST["name"]
        c = request.POST["contact"]
        e = request.POST["email"]
        a = request.POST["age"]
        g = request.POST["gender"]
        d = request.POST["description"]
        try:
            Enquiry.objects.create(name=n, contact=c, email=e, age=a, gender=g, description=d)
            error = "no"
        except:
            error = "yes"
    context = {"error": error}
    return render(request, 'gym/add_enq.html', context)


def recd_enq(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    enq = Enquiry.objects.all()
    context = {"enq": enq}
    return render(request, 'gym/recd_enq.html', context)


def delete_enq(request, pk):
    if not request.user.is_authenticated:
        return redirect('signin')
    enq = Enquiry.objects.get(id=pk)
    enq.delete()
    return redirect('recd_enq')

###############///////////////---------------CREATING PLAN VIEWS---------------\\\\\\\\\\\\\\\###############

def add_plan(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == "POST":
        n = request.POST["name"]
        a = request.POST["amount"]
        d = request.POST["duration"]
        try:
            Plan.objects.create(name=n, amount=a, duration=d )
            error = "no"
        except:
            error = "yes"
    context = {"error": error}
    return render(request, 'gym/add_plan.html', context)


def membership_plan(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    plan = Plan.objects.all()
    context = {"plan": plan}
    return render(request, 'gym/membership_plan.html', context)


def delete_plan(request, pk):
    if not request.user.is_authenticated:
        return redirect('signin')
    plan = Plan.objects.get(id=pk)
    plan.delete()
    return redirect('membership_plan')

###############///////////////---------------CREATING EQUIPMENT VIEWS---------------\\\\\\\\\\\\\\\###############


def add_equip(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == "POST":
        n = request.POST["name"]
        p = request.POST["price"]
        u = request.POST["unit"]
        d = request.POST["date"]
        dc = request.POST["description"]
        try:
            Equipment.objects.create(name=n, price=p, unit=u, date=d, description=dc)
            error = "no"
        except:
            error = "yes"
    context = {"error": error}
    return render(request, 'gym/add_equip.html', context)


def recd_equip(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    equip = Equipment.objects.all()
    context = {"equip": equip}
    return render(request, 'gym/recd_equip.html', context)


def delete_equip(request, pk):
    if not request.user.is_authenticated:
        return redirect('signin')
    equip = Equipment.objects.get(id=pk)
    equip.delete()
    return redirect('recd_equip')

###############///////////////---------------CREATING ENQUIRY VIEWS---------------\\\\\\\\\\\\\\\###############


def add_member(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == "POST":
        n = request.POST["name"]
        i = request.POST["member_id"]
        c = request.POST["contact"]
        ac = request.POST["alt_contact"]
        e = request.POST["email"]
        a = request.POST["age"]
        g = request.POST["gender"]
        p = request.POST["plan"]
        s = request.POST["shifting"]
        jd = request.POST["joining_date"]
        ed = request.POST["expiry_date"]
        ip = request.POST["initial_pay"]

        try:
            Member.objects.create(name=n, member_id=i, contact=c, alt_contact=ac, email=e, age=a, gender=g, plan=p, shifting=s, joining_date=jd, expiry_date=ed, initial_pay=ip)
            error = "no"
        except:
            error = "yes"
    context = {"error": error}
    return render(request, 'gym/add_member.html', context)


def recd_member(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    member = Member.objects.all()
    context = {"member": member}
    return render(request, 'gym/recd_member.html', context)


def delete_member(request, pk):
    if not request.user.is_authenticated:
        return redirect('signin')
    member = Member.objects.get(id=pk)
    member.delete()
    return redirect('recd_member')

def thank_you(request):
    return render(request, 'gym/thank_you.html')