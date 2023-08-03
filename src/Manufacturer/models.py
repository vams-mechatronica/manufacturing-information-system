from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(_("Manufacturer Name"), max_length=250)
    short_name = models.CharField(_("Manufacturer Short Name"), max_length=250)
    
    

    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

