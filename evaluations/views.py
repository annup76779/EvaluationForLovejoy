from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View

from evaluations.forms import EvaluationRequestForm


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
