from django import forms

class ProfileForm(forms.Form):
    """Create a form for collecting profiles."""
    user_image = forms.ImageField()