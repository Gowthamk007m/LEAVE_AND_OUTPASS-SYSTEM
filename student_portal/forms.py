from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('request_type', 'reason',
                  'leave_date_start', 'leave_date_end')
        widgets = {
            'request_type': forms.Select(choices=[
                ('leave', 'Leave'),
                ('outing', 'Outing'),
                ('extended_outing', 'Extended Outing'),
            ]),
            'reason': forms.Select(choices=[
                ('Illness', 'Illness'),
                ('Vacation', 'Vacation'),
                ('Family Emergency', 'Family Emergency'),
                ('Personal Reasons', 'Personal Reasons'),
                ('Wedding', 'Wedding'),
                ('Childcare', 'Childcare'),
                ('Bereavement', 'Bereavement'),
                ('Religious Observances', 'Religious Observances'),
                ('Other', 'Other'),
            ]),
            'leave_date_start': forms.DateInput(attrs={'type': 'date'}),
            'leave_date_end': forms.DateInput(attrs={'type': 'date'}),
        }

