from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.
def save_profile(request):
  if request.method=="POST":
      Profile.objects.create(
      name = request.POST.get('name'),
      email = request.POST.get('email'),
      phone = request.POST.get('phone'),
      degree = request.POST.get('degree'),
      school = request.POST.get('school'),
      university = request.POST.get('university'),
      summary = request.POST.get('summary'),
      previous_work = request.POST.get('previous_work'),
      skills = request.POST.get('skills'))
      return redirect('dashboard_view')

  return render(request, 'myapp/accept.html')

def resume(request, key):
  matched_profile = Profile.objects.get(id = key)
  return render(request, 'myapp/resume.html', {'user_profile' : matched_profile})

def dashboard(request):
  o = Profile.objects.all()
  return render(request, 'myapp/dashboard.html', {'resumes' : o})