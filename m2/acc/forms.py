from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import CustomUser


class regform(UserCreationForm):
    username = forms.CharField(required=True)  # (يتلغى)
    # stu_y = (
    #    (1, 'First'),
    #    (2, 'sdf'),
    #    (3, 'Fifsdfrst'),
    #    (4, 'Fisfddsfrst'),
    #)
    year = forms.IntegerField(max_value=4, min_value=1)  # (يتلغى)
    #year = forms.IntegerField(choices=stu_y, max_length=1)

    class Meta:
        #model = User    (يتلغى)
        model = CustomUser
        fields = (
            'username',
            'year',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(regform, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.year = self.cleaned_data['year']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()

        return user
