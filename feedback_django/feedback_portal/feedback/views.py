from django.shortcuts import render, redirect
from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Retrieve existing submissions list from session or initialize empty list
            submissions = request.session.get('feedback_submissions', [])
            
            # Append new submission dictionary
            new_submission = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'rating': form.cleaned_data['rating'],
                'comments': form.cleaned_data['comments'],
            }
            submissions.append(new_submission)
            
            # Save back to session
            request.session['feedback_submissions'] = submissions
            request.session.modified = True
            
            return redirect('results')
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})


def results_view(request):
    submissions = request.session.get('feedback_submissions', [])
    return render(request, 'feedback/results.html', {'submissions': submissions})
