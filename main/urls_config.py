from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('skills', views.skills, name='skills'),
    path('certifications', views.certifications, name="certifications"),
    path('hobby/', views.hobby, name="hobby"),
    path('contact', views.contact, name="contact"),
    path('resume/view/', views.view_resume, name='view_resume'),
    path('resume/download/', views.download_resume, name='download_resume'),
]
