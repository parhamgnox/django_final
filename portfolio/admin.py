from django.contrib import admin
from .models import *

class AdminServices(admin.ModelAdmin):

    list_display = ['title', 'content', 'price']
    list_filter = ['price']
    search_fields = ['title']

admin.site.register(Portfolio,AdminServices)
admin.site.register(Skills)
admin.site.register(Category)
admin.site.register(Team_Members)
admin.site.register(Comment)
admin.site.register(Reply)