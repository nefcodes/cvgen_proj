from django.urls import path
from . import views
urlpatterns = [
  path('', views.dashboard, name = "dashboard_view"),
  path('saveprofile', views.save_profile, name = "save_profile_view"),
  path('<int:key>/', views.resume, name = "resume_view"),

]