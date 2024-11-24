from django.urls import path

from evaluations.views import *

urlpatterns = [
    path('request/', RequestEvaluationView.as_view(), name='request_evaluation'),
    path('success/', SuccessPageView.as_view(), name='evaluation_success'),
]