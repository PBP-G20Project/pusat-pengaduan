from django import forms

class ReportForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    institution = forms.CharField(max_length=100)
    involved_party = forms.CharField(max_length=100)
    date = forms.DateTimeField()
    location = forms.CharField(max_length=100)
