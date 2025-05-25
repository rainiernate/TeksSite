from django.contrib import admin
from django.utils import timezone
from .models import Service, Testimonial, Post, ContactRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('order',)
    list_editable = ('order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'company', 'quote')
    list_editable = ('active',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date')
    list_filter = ('created_date', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_date'
    actions = ['publish_posts']
    
    def publish_posts(self, request, queryset):
        queryset.update(published_date=timezone.now())
    publish_posts.short_description = "Mark selected posts as published"

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('name', 'email', 'phone', 'message', 'created_date')
    date_hierarchy = 'created_date'
    
    def has_add_permission(self, request):
        return False
