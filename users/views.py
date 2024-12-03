from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View

from .forms import CustomUserForm
from .models import CustomUser
import logging

logger = logging.getLogger('custom')


class RegisterView(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email verification
            user.save()

            # Send verification email
            current_site = get_current_site(request)
            subject = 'Verify your email address'
            message = render_to_string('users/email_verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(subject, '', 'noreply@lovejoyantique.com', [user.email], html_message=message)

            return redirect('login')
        return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_invalid(self, form):
        # Add custom error message on invalid login
        form.add_error(None, "Invalid username or password.")
        return super().form_invalid(form)


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        logger.info(f"Password reset requested for email: {form.cleaned_data['email']}")
        return super().form_valid(form)


def verify_email(request, uid, token):
    try:
        uid = urlsafe_base64_decode(uid).decode()
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_verified = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Verification link is invalid or expired.')


@login_required
def logout_current_user_view(request):
    logout(request)
    return redirect("login")
