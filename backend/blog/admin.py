from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Category, Tag

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["photo_tag", "title", "category_set"]
    list_dislay_links = ["title"]
    
    def photo_tag(self, post):
        return mark_safe(f"<img src={post.photo.url} width=25% />")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
