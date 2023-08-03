from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Supplier(models.Model):
    supplier_code = models.CharField(_("Supplier's Code"), max_length=50,primary_key=True)
    mfg_supplier_name = models.CharField(_("Mfg. Supplier Name"), max_length=250)
    mfg_supplier_short_name = models.CharField(_("Short Name"), max_length=250,null=True,blank=True)
    address = models.TextField(_("Address"), max_length=1000)
    country = models.CharField(_("Country"), max_length=100)
    telephone = models.CharField(_("Telephone"), max_length=20)
    fax_number = models.CharField(_("Fax Number"), max_length=20,null=True,blank=True)
    email_id = models.EmailField(_("Email Id"), max_length=254)
    contact_person = models.CharField(_("Contact Person"), max_length=250)
    mobile_number = models.CharField(_("Mobile Number"), max_length=50)

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.mfg_supplier_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

