from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'submission_date')
    list_display_links = ('client',)
    search_fields = ('client__first_name',)

    fieldsets = [
        ('Testimonial Details', {'fields': ['client', 'message']}),
    ]


admin.site.register(Testimonial, TestimonialAdmin)