from django.contrib import admin
from .models import Specialty, Testimonial, Work, Partner, ContactMessage, SiteConfiguration


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'is_active', 'order']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'short_description']
    ordering = ['order']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'rating', 'is_active', 'order', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'rating']
    search_fields = ['name', 'service', 'text']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'procedure', 'is_active', 'order', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'procedure']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'order']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'service', 'is_read', 'created_at']
    list_filter = ['is_read', 'service']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['name', 'phone', 'email', 'service', 'datetime', 'message', 'created_at']
    ordering = ['-created_at']


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'phone', 'whatsapp']

    def has_add_permission(self, request):
        # Only allow one configuration
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
