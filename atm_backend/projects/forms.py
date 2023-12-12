from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "start_date",
            "end_date",
        ]
        widgets = {
            "end_date": forms.DateInput(attrs={"type": "date", "class": "date-input"}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": "date-input"}),
            "description": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }

    def clean_end_date(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        # Custom validation logic
        if end_date < start_date:
            raise forms.ValidationError("End date cannot be before start date.")
        return end_date
