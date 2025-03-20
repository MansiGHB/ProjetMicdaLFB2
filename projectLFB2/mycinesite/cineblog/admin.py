from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on','image')
    list_filter = ("status",)
    search_fields = ['title', 'content','image']
    prepopulated_fields = {'slug': ('title','image')}

admin.site.register(Post, PostAdmin)