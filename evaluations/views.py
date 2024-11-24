from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import View, ListView

from evaluations.forms import EvaluationRequestForm
from evaluations.models import EvaluationRequest


class RequestEvaluationView(LoginRequiredMixin, View):
    def get(self, request):
        form = EvaluationRequestForm()
        return render(request, 'evaluations/request_form.html', {'form': form})

    def post(self, request):
        form = EvaluationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.user = request.user
            evaluation.save()
            return redirect('evaluation_success')


class SuccessPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'evaluations/success.html')


class AdminRequestListView(UserPassesTestMixin, ListView):
    model = EvaluationRequest
    template_name = 'evaluations/admin_request_list.html'
    context_object_name = 'evaluations'
    paginate_by = 10  # Number of records per page
    ordering = ['-created_at']  # Orders evaluations by submission date (descending)

    def test_func(self):
        # Only allow access if the user is an admin (is_staff=True)
        return self.request.user.is_staff

    def handle_no_permission(self):
        # Redirect to the login page if the user is not an admin
        from django.shortcuts import redirect
        return redirect('/users/login/')

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        query = self.request.GET.get('q', '')
        start_date = self.request.GET.get('start_date', '')
        end_date = self.request.GET.get('end_date', '')
        user = self.request.GET.get('user', '')

        # Apply filters
        if query:
            queryset = queryset.filter(comment__icontains=query)
        if start_date:
            queryset = queryset.filter(created_at__gte=start_date)
        if end_date:
            queryset = queryset.filter(created_at__lte=end_date)
        if user:
            queryset = queryset.filter(user__username__icontains=user)
        return queryset
