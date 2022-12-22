from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate, gettext

from portfolio.models import Portfolio, Category, PortfolioImage, About


def home(request):
    return render(request, 'portfolio/home.html')


def my_stack(request):
    return render(request, 'portfolio/my_stack.html')


def about_me(request):
    about = About.objects.all()
    context = {'about': about}
    return render(request, 'portfolio/about_me.html', context)


def portfolio_index(request):
    portfolio = Portfolio.objects.all()
    paginator = Paginator(portfolio, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'portfolio/portfolio.html', context)


def view_portfolio(request, portfolio_id):
    portfolio_item = get_object_or_404(Portfolio, pk=portfolio_id)
    photos = PortfolioImage.objects.filter(case=portfolio_item)
    context = {'portfolio_item': portfolio_item, 'photos': photos}
    return render(request, 'portfolio/view_portfolio.html', context)


def get_category(request, category_id):
    portfolio = Portfolio.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    paginator = Paginator(portfolio, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'category': category}
    return render(request, 'portfolio/portfolio_category.html', context)
