from django.forms import ModelForm
from dashboard_admin.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = [
            "title",
            "content",
            "status"
            ]