from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

from .forms import CustomUserForm


class RegisterView(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_invalid(self, form):
        # Add custom error message on invalid login
        form.add_error(None, "Invalid username or password.")
        return super().form_invalid(form)