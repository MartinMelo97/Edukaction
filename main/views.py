from django.shortcuts import render
from django.views.generic import View

class Home(View):
	def get(self,request):
		template_name = "main/home.html"
		context = {}
		return render(request,template_name,context)