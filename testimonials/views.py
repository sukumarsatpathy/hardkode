from django.shortcuts import render
from .models import Testimonial


def testimonial(request):
    all_testimonials = Testimonial.objects.all().order_by('-submission_date')
    context = {
        'all_testimonials': all_testimonials,
    }
    return render(request, 'front/pages/testimonial.html', context)