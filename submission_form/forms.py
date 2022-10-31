from django.forms import ModelForm
from submission_form.models import Report

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = [
            "title",
            "content",
            "institution",
            "institution_level",
            "involved_party",
            "date",
            "location",
            ]
