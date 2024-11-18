from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from .models import UploadApplicant, InputApplicant
from django.utils.translation import gettext as _


class DocumentForm(forms.ModelForm):
    class Meta:
        model = UploadApplicant
        fields = [ 'document', 'ApplicantName', 'jobPosition', 'lampiranSKA', 'subklasifikasiSKA', 'klasifikasiSKA'  ]
    
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['ApplicantName'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['document'].widget.attrs.update({'class': 'form-control', 'required':'required', 'accept':'application/pdf,application' })
        self.fields['lampiranSKA'].widget.attrs.update({'class': 'form-control', 'accept':'application/pdf,application' })
        self.fields['subklasifikasiSKA'].widget.attrs.update({'class': 'form-control' })
        self.fields['klasifikasiSKA'].widget.attrs.update({'class': 'form-control', 'style':'text-align:center' })
        # self.fields['LastName'].widget.attrs.update({'class': 'form-control'})
        # self.fields['Gender'].widget.attrs.update({'class': 'form-select'})

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class DateInput(forms.DateInput):
    input_type = 'date'

class InputApplicantForm(forms.ModelForm):
    class Meta:
        model = InputApplicant
        fields = '__all__'
        widgets = {
            'DoB': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(InputApplicantForm, self).__init__(*args, **kwargs)
        self.fields['FirstName'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['LastName'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['Gender'].widget.attrs.update({
            'class': 'form-select',
            'required':'required'
            
        }, empty_label="Placeholder")
        self.fields['DoB'].widget.attrs.update({'class': 'form-control','required':'required' })
        self.fields['PoB'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['Nationality'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['personalEmail'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['personalMobile'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['linkedin'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['LicDrive'].widget.attrs.update({
            'class': 'form-select',
            'placeholder':'Jenis Kelamin',
            'required':'required'
            
        })
        self.fields['address_1'].widget.attrs.update({'class': 'form-control','required':'required'})
        self.fields['address_2'].widget.attrs.update({'class': 'form-control','required':'required'})
        self.fields['expectedSalary'].widget.attrs.update({'class': 'form-control','required':'required'})
        self.fields['grossSalary'].widget.attrs.update({'class': 'form-control','required':'required'})
        self.fields['medicalHistory'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['ReferensiInfo'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['referensiName'].widget.attrs.update({'class': 'form-control', 'required':'required'})
        self.fields['referensiRelasi'].widget.attrs.update({'class': 'form-control', 'required':'required'})

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(max_length=100,required=False, empty_value=None)
    groups = None
    user_permissions = None
    is_active = None
    is_superuser = None
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',

        )

class ModelFormWithFileField(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
