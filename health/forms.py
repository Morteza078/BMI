from django import forms


class BMIForm(forms.Form):
    weight = forms.FloatField()
    height = forms.FloatField()
