from django.urls import path
from .views import *
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', home, name='home'),
    path('stack/', my_stack, name='my_stack'),
    path('about/', about_me, name='about_me'),
    path('portfolio/', portfolio_index, name="portfolio_index"),
    path('portfolio/category/<int:category_id>/', get_category, name="portfolio_category"),
    path('portfolio/<int:portfolio_id>/', view_portfolio, name="view_portfolio")
]
