from django import forms
from .models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput

class FIRForm(forms.ModelForm):
    class Meta:
        model = FIRcode
        fields = '__all__'
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        