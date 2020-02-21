from bootstrap_datepicker_plus import DatePickerInput
from django import forms

FILE_CHOICES = [
    ('CallEntry To CDR', 'CallEntry To CDR'),
    ('CDR To CallEntry', 'CDR To CallEntry'),
    ('CALL ENTRY', 'CALL ENTRY'),
    ('CALL PROGRESS', 'CALL PROGRESS'),
    ('CDR', 'CDR'),
]

SERVER_CHOICES = [
    ('mysql', 'mysql'),
    ('MongoDB', 'MongoDB'),
    ('AWS', 'AWS'),
]


class UserForm(forms.Form):
    start_date = forms.DateTimeField(input_formats=['%d-%m-%Y'], widget=DatePickerInput())
    end_date = forms.DateTimeField(input_formats=['%d-%m-%Y'], widget=DatePickerInput())
    server = forms.CharField(label='Server', widget=forms.Select(choices=SERVER_CHOICES))
    file = forms.CharField(label='File', widget=forms.Select(choices=FILE_CHOICES))
