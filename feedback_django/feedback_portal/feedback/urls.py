from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='feedback', permanent=False)),
    path('feedback/', views.feedback_view, name='feedback'),
    path('results/', views.results_view, name='results'),
]
