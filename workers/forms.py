from django import forms
from .models import Worker


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = {
            'f_name',
            's_name',
            'position',
            'work_time',
            'cost_in_hour',
            'salary',
        }