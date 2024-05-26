from django.db import models
from django.urls import reverse
from Shop.models import *
from Suppliers.models import *
from Manufacturer.models import *
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from base64 import b64encode
from django_quill.fields import QuillField

# Create your models here.
class Equipment(models.Model):
    number = models.IntegerField(_("Equipemnt Number"))
    description = models.CharField(_("Description"), max_length=350)
    short_name = models.CharField(_("Short Name"), max_length=250,null=True, blank=True)
    shop_number = models.ForeignKey(Shop, verbose_name=_("Shop Number"), on_delete=models.CASCADE)
    bay = models.CharField(_("Bay"), max_length=50,null=True, blank=True)
    column = models.CharField(_("Column"), max_length=50,null=True, blank=True)
    section = models.CharField(_("Section"), max_length=50,null=True, blank=True)
    section_eln = models.CharField(_("Section ELN"), max_length=50,null=True, blank=True)
    equipment_type = models.CharField(_("Equipment Type"), max_length=50,null=True, blank=True,choices=(('A','A'), ('B','B'),  ('D','D'),('H','H')))
    sr_number = models.CharField(_("M/C Sr. No. Alloted by Mfg."), max_length=50,null=True, blank=True)
    model_number = models.CharField(_("M/C Model Number"), max_length=50,null=True, blank=True)
    manufacturer_code = models.ForeignKey(Manufacturer, verbose_name=_("Manufacturer Code"), on_delete=models.CASCADE,null=True, blank=True)
    supplier_code = models.ForeignKey(Supplier, verbose_name=_("Supplier Code"), on_delete=models.CASCADE,null=True, blank=True)
    indian_agent = models.BooleanField(_("Indian Agent"),null=True, blank=True)
    make = models.CharField(_("Make"), max_length=50,null=True, blank=True)
    cost = models.CharField(_("Cost"), max_length=50,null=True, blank=True)
    cost_in_lakhs = models.CharField(_("Cost in Lakhs"), max_length=50,null=True, blank=True)
    po_number = models.CharField(_("PO Number"), max_length=50,null=True, blank=True)
    po_date = models.DateField(_("PO Date"), auto_now=False, auto_now_add=False,null=True, blank=True)
    received_date = models.DateField(_("received date"), auto_now=False, auto_now_add=False)
    date_of_commissioning = models.DateField(_("Date of Commossioning"), auto_now=False, auto_now_add=False)
    ptc_issue_date = models.DateField(_("PTC Issue Date"), auto_now=False, auto_now_add=False,null=True, blank=True)
    warranty = models.CharField(_("Warranty(from the date of commissioning and proving out of MnP)"), max_length=50,null=True, blank=True)
    amc_covered_in_po = models.BooleanField(_("AMC covered in PO"),null=True, blank=True)
    amc_type = models.CharField(_("Type of AMC"), max_length=50,null=True, blank=True)
    amc_validity = models.DateField(_("Validity of AMC"), auto_now=False, auto_now_add=False,null=True, blank=True)
    recovery_value_warranty = models.CharField(_("Recovery Value in Warranty Period"), max_length=50,null=True, blank=True)
    percentage_avalability_in_warranty = models.CharField(_("%age Availability in Warranty Period"), max_length=50,null=True, blank=True)
    specification = models.TextField(_("Specifications"),max_length=5000,null=True, blank=True)
    machine_image = models.BinaryField(_("machine_image"), blank=True, null=True, editable=True)
    po_copy = models.BinaryField(
        verbose_name='po_copy', blank=True, null=True, editable=True)
    
    def scheme_machine_image_tag(self):
        if not self.machine_image:
            return ""
        return mark_safe('<img src = "data: image/png; base64, {}" width="200" height="100">'.format(
            b64encode(self.machine_image).decode('utf8')
        ))

    scheme_machine_image_tag.short_description = 'Machine Image'
    scheme_machine_image_tag.allow_tags = True

    def scheme_po_copy_tag(self):
        if not self.po_copy:
            return ""
        return mark_safe('<img src = "data: image/png; base64, {}" width="200" height="100">'.format(
            b64encode(self.po_copy).decode('utf8')
        ))

    scheme_po_copy_tag.short_description = 'PO Copy'
    scheme_po_copy_tag.allow_tags = True


    def __str__(self) -> str:
        return super().__str__()


    class Meta:
        verbose_name = _("Equipment")
        verbose_name_plural = _("Equipments")

    def get_absolute_url(self):
        return reverse("equipment-view")
    
class EquipmentSpare(models.Model):
    machine_number = models.ForeignKey(Equipment, verbose_name=_("M/C NO."), on_delete=models.CASCADE)
    part_list_number = models.IntegerField(_("PL No."))
    description = models.CharField(_("Sp. Description"), max_length=50)
    part_number = models.IntegerField(_("Part Number"))
    category = models.CharField(_("Category"), max_length=50)
    sp_d = models.CharField(_("SP D"), max_length=50)
    quantity = models.IntegerField(_("Quantity"))
    currency = models.CharField(_("Currency"), max_length=50)
    unit_price = models.FloatField(_("Unit Price"), max_length=40)
    total_price = models.FloatField(_("Total Price"),max_length=50)
    ledger_number = models.CharField(_("Ledger Detail"), max_length=50)
    remarks = models.CharField(_("Remarks"), max_length=500)
    

    class Meta:
        verbose_name = _("EquipmentSpare")
        verbose_name_plural = _("EquipmentSpares")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("equipment-spares-details", kwargs={"pk": self.pk})

class EquipmentStatics(models.Model):
    machine_number = models.ForeignKey(Equipment, verbose_name=_("Identification Number"), on_delete=models.CASCADE)
    flag = models.BooleanField(_("FLAG"),default=True)
    at_number = models.CharField(_("AT. No."), max_length=100)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    date_of_commissionning = models.DateField(_("Date of Commissionning"), auto_now=False, auto_now_add=False)
    phone = models.CharField(_("Phone"), max_length=50)
    contact_person = models.CharField(_("Contact Person"), max_length=50)
    location = models.ForeignKey(Shop, verbose_name=_("Location"), on_delete=models.CASCADE)
    fax = models.CharField(_("FAX"), max_length=50,null=True,blank=True)
    technical_parameters = QuillField(null=True, blank=True)
    present_usage = QuillField(null=True, blank=True)

    

    class Meta:
        verbose_name = _("EquipmentStatics")
        verbose_name_plural = _("EquipmentStatics")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("EquipmentStatics_detail", kwargs={"pk": self.pk})
