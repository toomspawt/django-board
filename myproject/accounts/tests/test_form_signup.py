from django.test import TestCase
from ..forms import SignUpForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        """
        Awareness for future change of form
        """
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2']
        got = list(form.fields)
        self.assertSequenceEqual(expected, got)