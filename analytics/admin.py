from django.contrib import admin

# my models
from analytics.models import AccessForAnalytics

class AccessForAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['value_page', 'page', 'accessed_at', 'ip']
    
admin.site.register(AccessForAnalytics, AccessForAnalyticsAdmin)