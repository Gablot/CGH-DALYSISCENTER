from django.urls import path
from . import views


urlpatterns = [
	path('',views.home, name="home"),
	path('Home.html',views.home, name="home"),
	path('contact.html',views.contact, name="contact"),
	path('about.html',views.about, name="about"),
	path('pricing.html',views.pricing, name="pricing"),
	path('services.html',views.services, name="services"),
	path('Schedule.html',views.Schedule, name="Schedule"),
	path('ScheduleSchedule.html',views.ScheduleSchedule, name="ScheduleSchedule"),
]
