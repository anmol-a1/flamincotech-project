from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from Admin1.models import NewUser
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.hashers import make_password
from .utils import Util
import datetime
def password_reset_request(request):
	print("start1")
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		print("start2")

		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			print("start3")

			associated_users = NewUser.objects.filter(Q(email=data))
			if associated_users.exists():
				print("start4")
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'rahulraut0990@gmail.com' , [user.email], fail_silently=False)
						# data = {'email_body': subject, 'to_email': email,'email_subject': 'Reset your passsword'}
						# Util.send_email(data)
						print("sent")
					except BadHeaderError:
						print("start5")
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})