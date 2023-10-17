from django.shortcuts import render , redirect
from .models import *
from portfolio.models import Portfolio,Team_Members,Category
from accounts.models import CustomeUser
from .forms import ContactUsForm , NewsLetterForm
from django.contrib import messages

def home(request):
    if request.method == 'GET':
    

        service_count = Services.objects.filter(status=True).count()
        portfolio_count = Portfolio.objects.filter(status=True).count()
        team_mem_count = Team_Members.objects.filter(status=True).count()
        user_count = CustomeUser.objects.filter(is_active=True).count()
        services = Services.objects.filter(status=True)
        four_services = Services.objects.filter(status=True)[:4]
        popular_portfolio = Portfolio.objects.filter(status=True)[:3]
        category = Category.objects.all()
        team_members = Team_Members.objects.filter(status=True)[:3]
        context = {
            'service': services,
            'fservice': four_services,
            'p_portfolios': popular_portfolio,
            'team_members': team_members,
            'category': category,
            'sc': service_count,
            'pc': portfolio_count,
            'tc': team_mem_count,
            'uc': user_count,

        }
        return render(request,"root/index.html",context=context)

    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():

            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submitted successfully')
            return redirect('root:home')

        else:
            messages.add_message(request,messages.ERROR,'invalid email address')
            return redirect('root:home')
        
    elif request.method == 'POST' and len(request.POST) == 5 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
 
            form.save()
            messages.add_message(request,messages.SUCCESS,'we received your message and we call with you as soon as possible')
            return redirect('root:home')

        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect('root:home')

def about(request):
    if request.method == 'GET':
 
        category = Category.objects.all()
    
        context = {
            'category':category,
        }
    
        return render(request,"root/about.html",context=context)
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():

            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submitted successfully')
            return redirect('root:about')

        else:
            messages.add_message(request,messages.ERROR,'invalid email address')
            return redirect('root:about')
        
    elif request.method == 'POST' and len(request.POST) == 5 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
 
            form.save()
            messages.add_message(request,messages.SUCCESS,'we received your message and we call with you as soon as possible')
            return redirect('root:about')

        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect('root:about')


def contact(request):
    if request.method == 'GET':
        category = Category.objects.all()
    
        context = {
            'category':category,
        }
    
        return render(request,"root/contact.html",context=context)

    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():

            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submitted successfully')
            return redirect('root:contact')

        else:
            messages.add_message(request,messages.ERROR,'invalid email address')
            return redirect('root:contact')
        
    elif request.method == 'POST' and len(request.POST) == 5 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
 
            form.save()
            messages.add_message(request,messages.SUCCESS,'we received your message and we call with you as soon as possible')
            return redirect('root:contact')

        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect('root:contact')


def team_members(request):
    if request.method == 'GET':
        category = Category.objects.all()
        team_members = Team_Members.objects.filter(status=True)[:3]
        context = {
            'category' : category,
            'team_members' : team_members,
        }
    
        return render(request,"root/team_members.html",context=context) 
    
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():

            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submitted successfully')
            return redirect('root:team_members')

        else:
            messages.add_message(request,messages.ERROR,'invalid email address')
            return redirect('root:team_members')
        
    elif request.method == 'POST' and len(request.POST) == 5 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
 
            form.save()
            messages.add_message(request,messages.SUCCESS,'we received your message and we call with you as soon as possible')
            return redirect('root:team_members')

        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect('root:team_members')