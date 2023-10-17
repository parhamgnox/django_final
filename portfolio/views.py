from django.shortcuts import render, get_object_or_404 , redirect
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from root.forms import ContactUsForm , NewsLetterForm
from django.contrib import messages
from .forms import CommentForm , ReplyForm
from django.contrib.auth.decorators import login_required


def portfolio(request,cat=None, team=None):
    
    if request.method == 'GET':
    
        if cat:
            portfolio = Portfolio.objects.filter(category__name = cat)
        elif team:
            portfolio = Portfolio.objects.filter(team_member__info__username = team)
        elif request.GET.get('search'):
            portfolio = Portfolio.objects.filter(content__contains=request.GET.get('search'))
        else:
            portfolio = Portfolio.objects.filter(status=True)




        portfolio = Paginator(portfolio,2)
        first_page = 1
        last_page = portfolio.num_pages
        category = Category.objects.all()
        
        try:
            page_number = request.GET.get('page')
            portfolio = portfolio.get_page(page_number)

        except EmptyPage:
            portfolio = portfolio.get_page(1) 

        except PageNotAnInteger:
            portfolio = portfolio.get_page(1)                              
        
        context = {
            'portfolios' : portfolio,
            'portfolio':portfolio,
            'category':category,
            'first_page':first_page,
            'last_page':last_page,

        }
    
        return render(request,'portfolio/portfolio.html',context=context)

    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():

            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submitted successfully')
            return redirect('root:portfolio')

        else:
            messages.add_message(request,messages.ERROR,'invalid email address')
            return redirect('root:portfolio')
        
    elif request.method == 'POST' and len(request.POST) == 5 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
 
            form.save()
            messages.add_message(request,messages.SUCCESS,'we received your message and we call with you as soon as possible')
            return redirect('root:portfolio')

        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect('root:portfolio')



def portfolio_details(request,id):
    if request.method == 'GET':
        try:
            portfolio = Portfolio.objects.get(id=id) 
            comments = Comment.objects.filter(which_portfolio=id,status=True)
            reply = Reply.objects.filter(status=True)
            id_list = []
            portfolios = Portfolio.objects.filter(status=True)
            for pr in portfolios:
                id_list.append(pr.id)

            id_list.reverse()
        
            if id_list[0] == id:
                next_portfolio = Portfolio.objects.get(id=id_list[0])
                previous_portfolio = None 

            elif id_list[-1] == id:
                next_portfolio = None
                previous_portfolio = Portfolio.objects.get(id=id_list[-2])

            else:   
                next_portfolio = Portfolio.objects.get(id=id_list[id_list.index(id)+1])
                previous_portfolio = Portfolio.objects.get(id=id_list[id_list.index(id)-1])

            portfolio.counted_views += 1
            portfolio.save()
            context = {"portfolio": portfolio,
                       'next_portfolio' : next_portfolio,
                       'previous_portfolio' :  previous_portfolio,
                       'comments': comments,
                       'reply' : reply,
            }
            return render(request,'portfolio/portfolio-details.html',context=context)
        except:
            return render(request,'portfolio/404.html')

    elif request.method == 'POST' and len(request.POST) > 2:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment has submitted and published as soon')
            return redirect(request.path_info)
            
        else:
            messages.add_message(request,messages.ERROR,'yor comment data is not valid')
            return redirect (request.path_info)



@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    cid = comment.which_portfolio.id
    comment.delete()
    return redirect(f'/portfolio/portfolio_details/{cid}')

@login_required
def edit(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        

        context = {
            'comment' : comment,
        }
        return render(request,'portfolio/edit.html',context=context)
    
    elif request.method == 'POST' :
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            cid = comment.which_portfolio.id
            return redirect (f'/portfolio/portfolio_details/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'chete baba ba in data dadanet .... zereshk')
            return redirect(request.path_info)

@login_required
def reply(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        form = ReplyForm()

        context = {
            'comment' : comment,
            'form' : form,
        }
        return render(request,'portfolio/reply.html',context=context)
    
    elif request.method == 'POST' :
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            cid = comment.which_portfolio.id
            return redirect (f'/portfolio/portfolio_details/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'chete baba ba in data dadanet .... zereshk')
            return redirect (request.path_info)