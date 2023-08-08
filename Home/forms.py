from django import forms

# Create your forms here.


class CustomerForm(forms.Form):
    name = forms.CharField(initial="Full Name",max_length=550)
    email = forms.CharField(initial="Email",max_length=300)
    phno = forms.CharField(initial="+91",max_length=12)
    services = forms.CharField(initial="",max_length=600)
