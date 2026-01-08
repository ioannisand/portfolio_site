from django.shortcuts import render
from .models import Profile
from resume.models import Skill, Experience, Certificate, Education  # <-- Added Education
from projects.models import Project


def home(request):
    profile = Profile.objects.first()

    # Projects
    featured_projects = Project.objects.filter(is_featured=True).order_by('-date_created')[:3]

    # Skills
    featured_skills = Skill.objects.filter(is_featured=True)

    # Experience (Jobs)
    latest_experience = Experience.objects.all().order_by('-start_date')[:3]

    # NEW: Education (Your Biotech background + Self Taught journey)
    education_list = Education.objects.all().order_by('-start_date')

    # NEW: Certificates (The proof of your skills)
    # We take the top 4 most recent ones for the homepage
    latest_certs = Certificate.objects.all().order_by('-date_issued')[:4]

    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'featured_skills': featured_skills,
        'latest_experience': latest_experience,
        'education_list': education_list,  # <-- Added to context
        'latest_certs': latest_certs,  # <-- Added to context
    }

    return render(request, 'core/home.html', context)