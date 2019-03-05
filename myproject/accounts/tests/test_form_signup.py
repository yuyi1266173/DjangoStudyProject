from django.test import TestCase

from accounts.forms import SignUpForm


class SignUpFormTests(TestCase):

    def test_form_has_fields(self):
        form = SignUpForm()
        excepted = ['username', 'email', 'password1', 'password2', ]
        actual = list(form.fields)
        self.assertSequenceEqual(excepted, actual)
