from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)
    profile_picture = forms.ImageField()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'profile_picture', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile(
                user=user,
                address_line1=self.cleaned_data['address_line1'],
                city=self.cleaned_data['city'],
                state=self.cleaned_data['state'],
                pincode=self.cleaned_data['pincode'],
                profile_picture=self.cleaned_data['profile_picture'],
            )
            profile.save()
        return user
