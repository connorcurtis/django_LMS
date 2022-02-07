from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from datetime import date
from django.forms import ModelForm, Select
from .models import *
from django.db.models import Q, F


class RegistrationForm(UserCreationForm):
    bool_choices = ((1, 'Instructor'), (0, 'Student'))

    is_instructor = forms.TypedChoiceField(
        choices=bool_choices, widget=forms.RadioSelect, coerce=int
    )

    def clean_birthday(self):
        bday = self.cleaned_data['birthday']
        age = (date.today() - bday).days / 362
        if age < 16:
            raise forms.ValidationError('Must be at least 16 years old to register')
        return bday

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'birthday', 'is_instructor']


class ImageForm(forms.ModelForm):

    class Meta:
        model = UserImage
        fields = ['image']


choices = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
           ('Friday', 'Friday'))


class CourseForm(ModelForm):
    #choice = forms.CharField(choices=choices, widget=forms.CheckboxSelectMultiple

    class Meta:
        model = Course
        widgets = {'meeting_time_days': forms.CheckboxSelectMultiple}
        fields = ['department', 'course_number', 'course_name',  'credit_hours', 'meeting_time_days', 'start_time', 'end_time']


class ProfileEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'birthday', 'addressLine1', 'addressLine2', 'city', 'bio',
                  'link1', 'link2', 'link3']


class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class AdminUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class EditProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birthday', 'phone_number', 'addressLine1',
                  'addressLine2', 'city', 'bio', 'link1', 'link2', 'link3']


class StudentEnrollForm(ModelForm):
    class Meta:
        model = Course
        fields = ['department']
