from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from base64 import b64encode
from django_quill.fields import QuillField
from django.urls import reverse
from Equipment.models import Equipment

# Create your models here.
class OilMaster(models.Model):
    pl_no = models.CharField(_("PL No."), max_length=50)
    machine = models.ForeignKey(Equipment, verbose_name=_("Machine"), on_delete=models.CASCADE)
    flag = models.CharField(_("Flag"), max_length=50,null=True,blank=True)
    date = models.DateField(_("date"), auto_now=False, auto_now_add=False)
    qty_received = models.IntegerField(_("Quantity Received"))
    qty_issued = models.IntegerField(_("Quantity Issued"))
    meter_reading = models.DecimalField(_("Meter Read"), max_digits=7, decimal_places=2)
    unit = models.IntegerField(_("Unit"))
    remarks = models.TextField(_("Remarks"))    

    class Meta:
        verbose_name = _("OilMaster")
        verbose_name_plural = _("OilMasters")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("OilMaster_detail", kwargs={"pk": self.pk})
