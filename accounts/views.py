from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

class LogoutView (View):
	def post (self, request, *args, **kwargs):
		logout(request)
		return redirect('index')

class ChangePassword(View):
	template_name = 'accounts/change_password.html'
	def post (self, request, *args, **kwargs):
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('index')
	def get (self, request, *args, **kwargs):
		form = PasswordChangeForm(request.user)
		return render(request, self.template_name, {'form': form})

class SignUpView(View):
	template_name = 'accounts/signup.html'
	def post (self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	def get (self, request, *args, **kwargs):
		form = UserCreationForm()
		return render(request, self.template_name, {'form': form})

class IndexView(View):
	template_name = 'accounts/index.html'
	def get (self, request, *args, **kwargs):
		return render(request, self.template_name, {})
