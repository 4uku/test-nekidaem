from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Blog, BlogFollow, CustomUser, Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogFollow)
class BlogFollowAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
