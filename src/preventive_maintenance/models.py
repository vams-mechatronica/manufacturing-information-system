from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from Equipment.models import Equipment
from Shop.models import FIRcode

# Create your models here.
class PMActivityMaster(models.Model):
    no = models.IntegerField(_("activity no"),primary_key=True)
    description = models.TextField(_("description"))
    schd_class = models.CharField(_("schd class"), max_length=50,null=True, blank=True)
    remarks = models.CharField(_("remarks"), max_length=500,null=True, blank=True)
    iso = models.CharField(_("iso"), max_length=500,null=True, blank=True)

    class Meta:
        verbose_name = _("PMActivityMaster")
        verbose_name_plural = _("PMActivityMasters")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PMActivityMaster_detail", kwargs={"pk": self.pk})


class PMSchedule(models.Model):
    maint_ord = models.IntegerField(_("Maint Ord"),default=100,null=True, blank=True)
    machine = models.ForeignKey(Equipment, verbose_name=_(""), on_delete=models.CASCADE)
    schedule_due_date = models.DateField(_("Schedule Due Date"), auto_now=False, auto_now_add=False)
    schedule_class = models.CharField(_("Schd Class"), max_length=50,null=True,blank=True)
    

    class Meta:
        verbose_name = _("PMSchedule")
        verbose_name_plural = _("PMSchedules")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("PMSchedule_detail", kwargs={"pk": self.pk})

class PMScheduleFeedback(models.Model):
    schedule = models.ForeignKey(PMSchedule, verbose_name=_("Schedule Id"), on_delete=models.CASCADE)
    flag = models.BooleanField(_("Flag"),default=False)
    start_time = models.DateTimeField(_("Date of Beginning"), auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(_("Date of Ending"), auto_now=False, auto_now_add=False)
    spare_issued = models.TextField(_("Spare Issued"))
    remarks = models.TextField(_("Remarks"))

    class Meta:
        verbose_name = _("PMScheduleFeedback")
        verbose_name_plural = _("PMScheduleFeedbacks")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("PMScheduleFeedback_detail", kwargs={"pk": self.pk})

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


class BreakDown(models.Model):
    flag = models.CharField(_("Flag"), max_length=50,choices=(('Y','Y'),('M','M'),('N','N')))
    machine = models.ForeignKey(Equipment, verbose_name=_(""), on_delete=models.CASCADE)
    break_down_date = models.DateTimeField(_("Break down Datetime"), auto_now=False, auto_now_add=False)
    fir_code = models.ForeignKey(FIRcode, verbose_name=_("FIR"), on_delete=models.CASCADE,null=True,blank=True)
    fault_reported = models.CharField(_("Fault"), max_length=500)
    up_date_time = models.DateTimeField(_("Up datetime"), auto_now=False, auto_now_add=False)
    total_breakdown_hrs = models.DecimalField(_("breakdown hrs"), max_digits=5, decimal_places=2)
    cause_code = models.CharField(_("cause_code"), max_length=500,null=True, blank=True,choices=(('M','M'),('E','E')))
    reason = models.TextField(_("Reason"))
    description_of_mtc_activity_done = models.TextField(_("Description of Maintenance Activity Done"))
    

    class Meta:
        verbose_name = _("BreakDown")
        verbose_name_plural = _("BreakDowns")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("BreakDown_detail", kwargs={"pk": self.pk})
