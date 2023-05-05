from django.http import HttpResponse
from django.shortcuts import render
from .models import WorkExperience, Education, Skill


def home(request):
    return render(request, 'myresume/home.html')


def work(request):
    work_experience = WorkExperience.objects.all()
    context = {'work_experience': work_experience}
    return render(request, 'myresume/work.html', context)


def education(request):
    education = Education.objects.all()
    context = {'education': education}
    return render(request, 'myresume/education.html', context)


def skills(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'myresume/skills.html', context)

def view_pdf(request):
    with open('path/to/your/pdf/file.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename="file.pdf"'
        return response