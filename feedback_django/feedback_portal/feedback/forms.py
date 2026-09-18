from django import forms


class FeedbackForm(forms.Form):
    RATING_CHOICES = [
        ('1', '1 - Poor'),
        ('2', '2 - Fair'),
        ('3', '3 - Good'),
        ('4', '4 - Very Good'),
        ('5', '5 - Excellent'),
    ]

    name = forms.CharField(
        label="Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name',
        })
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@example.com',
        })
    )

    rating = forms.ChoiceField(
        label="Rating",
        choices=RATING_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )

    comments = forms.CharField(
        label="Comments",
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Share your feedback here...',
        })
    )
