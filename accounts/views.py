from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm

# Create your views here.
class Registro(View):
	def get(self,request):
		template_name = "accounts/registration.html"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "accounts/registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()
			return redirect('edukaction.html')
		else:
			context = {
			'form':new_user_form
			}
			return render(request.template_name,context)
