from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # list_display = ["title", "tags", "owner", "is_public", "photo", "date_created"]
    list_display = [field.name for field in Post._meta.fields]

admin.site.register(Post, PostAdmin)