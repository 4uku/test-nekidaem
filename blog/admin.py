from django.contrib import admin

from .models import Blog, CustomUser, Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
