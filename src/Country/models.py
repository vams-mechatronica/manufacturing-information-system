from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Country(models.Model):
    name = models.CharField(_("Country Name"),max_length=100)
    code = models.CharField(_("Country Code"),max_length=2, unique=True)
    telephone_code = models.CharField(_("Telephone code"), max_length=50)
    
    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countrys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Country_detail", kwargs={"pk": self.pk})
