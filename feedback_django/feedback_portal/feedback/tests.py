from django.test import TestCase, Client
from django.urls import reverse


class FeedbackPortalTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_feedback_page_get(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback_form.html')
        self.assertContains(response, 'Feedback Portal')
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_valid_submission(self):
        """TEST 1 — Valid submission"""
        data = {
            'name': 'Sailu Velusuri',
            'email': 'sailu@example.com',
            'rating': '5',
            'comments': 'Excellent feedback portal.'
        }
        response = self.client.post(reverse('feedback'), data)
        # Should redirect to /results/
        self.assertRedirects(response, reverse('results'))

        # Check results page content
        results_response = self.client.get(reverse('results'))
        self.assertEqual(results_response.status_code, 200)
        self.assertContains(results_response, 'Sailu Velusuri')
        self.assertContains(results_response, 'sailu@example.com')
        self.assertContains(results_response, '5')
        self.assertContains(results_response, 'Excellent feedback portal.')

    def test_invalid_email(self):
        """TEST 2 — Invalid email"""
        data = {
            'name': 'Sailu',
            'email': 'invalid-email',
            'rating': '5',
            'comments': 'Test'
        }
        response = self.client.post(reverse('feedback'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback_form.html')
        self.assertContains(response, 'text-danger')
        self.assertContains(response, 'Enter a valid email address.')

    def test_empty_fields(self):
        """TEST 3 — Empty fields"""
        data = {
            'name': '',
            'email': '',
            'rating': '',
            'comments': ''
        }
        response = self.client.post(reverse('feedback'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback_form.html')
        self.assertContains(response, 'text-danger')
        self.assertContains(response, 'This field is required.')

    def test_multiple_submissions(self):
        """TEST 4 — Multiple submissions"""
        submission1 = {
            'name': 'Sailu Velusuri',
            'email': 'sailu@example.com',
            'rating': '5',
            'comments': 'First feedback comment'
        }
        submission2 = {
            'name': 'Alex Johnson',
            'email': 'alex@example.com',
            'rating': '4',
            'comments': 'Second feedback comment'
        }
        
        self.client.post(reverse('feedback'), submission1)
        self.client.post(reverse('feedback'), submission2)

        results_response = self.client.get(reverse('results'))
        self.assertEqual(results_response.status_code, 200)
        self.assertContains(results_response, 'Sailu Velusuri')
        self.assertContains(results_response, 'First feedback comment')
        self.assertContains(results_response, 'Alex Johnson')
        self.assertContains(results_response, 'Second feedback comment')
