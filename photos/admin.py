from django.contrib import admin
from .models import Category,Location,Image

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)
