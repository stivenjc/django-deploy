from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row
from django import forms
from django.contrib.auth.models import User

from twitter.models import Post, Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'content',
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['content'].label = 'insgrese contenido aqui'
            self.fields['content'].widget.attrs['placeholder'] = 'ingrese un texto'
            self.helper.layout = Layout(
                Row(
                    Column('content', css_class='col-md-12'),
                    css_class='form-row'
                ),
            )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
