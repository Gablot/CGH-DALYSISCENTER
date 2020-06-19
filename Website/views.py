from django.shortcuts import render
from django.core.mail import send_mail
from .models import Patient
def home(request):
	return render(request, 'Home.html', {}) 

def contact(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_email = request.POST['email']
		message_subject = request.POST['subject']
		message = request.POST['message']

	#Send Email
		send_mail(
			message_subject,#Subject
			message,#Message
			message_email,#From email
			['khylecarabio@gmail.com'],#To Email
			)


		return render(request, 'contact.html', {'name_': message_name})
	else:
		return render(request, 'contact.html', {}) 

def about(request):
	return render(request, 'about.html', {}) 

def pricing(request):
	return render(request, 'pricing.html', {}) 

def services(request):
	return render(request, 'services.html' , {}) 

def Schedule(request):

	PatientList = Patient.objects.all()


	return render(request, 'Schedule.html' , {'PatientList':PatientList})

def ScheduleSchedule(request):
	return render(request, 'ScheduleSchedule.html' , {})