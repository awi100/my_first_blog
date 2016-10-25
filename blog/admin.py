from django.contrib import admin
from .models import Post

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "published_date", "author"]
    search_fields = ["title", "content"]
    list_filter = ["published_date"]
        
admin.site.register(Post)
