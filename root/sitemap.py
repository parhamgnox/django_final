from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from portfolio.models import Portfolio

class StaticSiteMap(Sitemap):


    priority = 0.4
    changefreq = 'daily'

    def items(self):
        return [
            'root:home',
            'root:about',
            'root:contact',
            'root:team_members',
            'portfolio:portfolio',
        ]
    
    def location(self,item):
        return reverse(item)
    
class DynamicSiteMap(Sitemap):


    priority = 0.4
    changefreq = 'daily'

    def items(self):
        return Portfolio.objects.filter(status=True)

        
    
    def location(self,obj):
        return '/portfolio/portfolio_details/%s' % obj.id

