from django.urls import path
from .views import *

app_name = 'portfolio'

urlpatterns = [
    path("",portfolio , name='portfolio'),
    path("portfolio_details",portfolio_details, name='portfolio_details'),
    path("category/<str:cat>",portfolio,name="portfolio_cat"),
    path("team_member/<str:team>",portfolio,name="portfolio_team"),
    path("portfolio_details/<int:id>",portfolio_details,name="portfolio_details"),

]




