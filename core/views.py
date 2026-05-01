from django.shortcuts import render
from .models import Profile
from resume.models import Skill, Experience, Certificate
from projects.models import Project


def home(request):
    profile = Profile.objects.first()

    featured_projects = Project.objects.filter(is_featured=True).order_by('-date_created')[:6]
    featured_skills = Skill.objects.filter(is_featured=True)

    journey_items = []
    for exp in Experience.objects.all():
        journey_items.append({
            'kind': 'experience',
            'date': exp.start_date,
            'obj': exp,
        })
    for cert in Certificate.objects.all():
        journey_items.append({
            'kind': 'certificate',
            'date': cert.date_issued,
            'obj': cert,
        })
    journey_items.sort(key=lambda x: x['date'], reverse=True)

    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'featured_skills': featured_skills,
        'journey_items': journey_items,
    }

    return render(request, 'core/home.html', context)
