from django.shortcuts import render
from accounts.models import UserProfile
from testimonials.models import Testimonial


def home(request):
    hk_team = UserProfile.objects.filter(user_type='Team').order_by('created_date')
    all_testimonials = Testimonial.objects.all().order_by('submission_date')
    context = {
        'hk_team': hk_team,
        'all_testimonials': all_testimonials,
    }
    return render(request, 'front/pages/home.html', context)


def about(request):
    hk_team = UserProfile.objects.filter(user_type='Team').order_by('created_date')
    all_testimonials = Testimonial.objects.all().order_by('submission_date')
    context = {
        'hk_team': hk_team,
        'all_testimonials': all_testimonials,
    }
    return render(request, 'front/pages/about.html', context)


def service(request):
    return render(request, 'front/services/landing-page.html')


def webDevlopment(request):
    return render(request, 'front/services/category/web-development.html')


def project(request):
    return render(request, 'front/pages/project.html')


def contact(request):
    return render(request, 'front/pages/contact.html')