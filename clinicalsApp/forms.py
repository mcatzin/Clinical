from django import forms
from clinicalsApp.models import ClinicalData, Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'age': forms.TextInput(attrs={'class': 'input'}),
        #     'gender': forms.TextInput(attrs={'class': 'input'})
        # }
    name = forms.TextInput(attrs={'id': 'name',  'class': 'form-input'})
    age = forms.NumberInput(attrs={'id': 'age',  'class': 'form-input'})


class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        fields = '__all__'

    name = forms.TextInput(attrs={'id': 'name',  'class': 'form-input'})
