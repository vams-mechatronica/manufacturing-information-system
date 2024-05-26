from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Shop(models.Model):
    shop_no = models.IntegerField(_("Shop Number"),primary_key=True)
    shop_name = models.CharField(_("Shop Name"), max_length=250)
    shop_short_name = models.CharField(_("Shop Short Name"), max_length=250)
    

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")

    def __str__(self):
        return self.shop_name

    def get_absolute_url(self):
        return reverse("Shop_detail", kwargs={"pk": self.pk})

class FIRcode(models.Model):
    number = models.IntegerField(_("FIR Code number"),primary_key=True)
    description = models.CharField(_("Description"), max_length=350)

    class Meta:
        verbose_name = _("FIRcode")
        verbose_name_plural = _("FIRcodes")

    def __str__(self):
        return self.fir_code_number

    def get_absolute_url(self):
        return reverse("FIRcode_detail", kwargs={"pk": self.pk})
