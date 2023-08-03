from django.contrib import admin
from .models import *
from django import forms
# Register your models here.
class ItemForm(forms.ModelForm):
    machine_image = forms.FileField(required=False)
    po_copy = forms.FileField(required=False)

    def save(self, commit=True):
        if self.cleaned_data.get('machine_image') is not None \
                and hasattr(self.cleaned_data['machine_image'], 'file'):
            data = self.cleaned_data['machine_image'].file.read()
            self.instance.machine_image = data
        
        if self.cleaned_data.get('po_copy') is not None \
                and hasattr(self.cleaned_data['po_copy'], 'file'):
            data = self.cleaned_data['po_copy'].file.read()
            self.instance.po_copy = data

        return self.instance

    def save_m2m(self):
        # FIXME: this function is required by ModelAdmin, otherwise save process will fail
        pass


class EquipmentAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ('number', 'scheme_machine_image_tag','scheme_po_copy_tag')

admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(EquipmentSpare)
admin.site.register(EquipmentStatics)