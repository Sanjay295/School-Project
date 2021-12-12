from django import forms
class StudForm(forms.Form):
    s_name = forms.CharField(max_length=30)
    f_name = forms.CharField(max_length=30)
    s_DOB = forms.IntegerField()
    s_class = forms.CharField(max_length=30)
    s_address = forms.CharField(max_length=30)
    s_school = forms.CharField(max_length=30)
    s_email = forms.EmailField(max_length=30)
    s_city = forms.CharField(max_length=30)
    s_state = forms.CharField(max_length=30)
    s_pin = forms.IntegerField()

class SForm(forms.Form):
    s_name = forms.CharField(max_length=30)
