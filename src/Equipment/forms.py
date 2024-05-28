from django import forms
from .models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            "po_date": DatePickerInput(options={"format": "MM/DD/YYYY"}),
            "ptc_issue_date": DatePickerInput(options={"format": "MM/DD/YYYY"}),
            "received_date": DatePickerInput(options={"format": "MM/DD/YYYY"}),
            "date_of_commissioning": DatePickerInput(options={"format": "MM/DD/YYYY"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        # Update widgets for file fields
        self.fields['machine_image'].widget = forms.ClearableFileInput(attrs={'class': 'form-control'})
        self.fields['po_copy'].widget = forms.ClearableFileInput(attrs={'class': 'form-control'})