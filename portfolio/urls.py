from django.urls import path
from .views import *

app_name = 'portfolio'

urlpatterns = [
    path("",portfolio , name='portfolio'),
    path("portfolio_details",portfolio_details, name='portfolio_details'),
    path("category/<str:cat>",portfolio,name="portfolio_cat"),
    path("team_member/<str:team>",portfolio,name="portfolio_team"),
    path("portfolio_details/<int:id>",portfolio_details,name="portfolio_details"),
    path("<int:id>",delete_comment,name="delete"),
    path("edit/comment/<int:id>",edit,name="edit"),
    path("comment/reply/<int:id>",reply,name="reply"),
]




