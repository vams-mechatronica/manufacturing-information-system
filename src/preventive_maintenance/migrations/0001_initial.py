# Generated by Django 4.2.4 on 2024-05-26 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0001_initial'),
        ('Equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PMActivityMaster',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False, verbose_name='activity no')),
                ('description', models.TextField(verbose_name='description')),
                ('schd_class', models.CharField(blank=True, max_length=50, null=True, verbose_name='schd class')),
                ('remarks', models.CharField(blank=True, max_length=500, null=True, verbose_name='remarks')),
                ('iso', models.CharField(blank=True, max_length=500, null=True, verbose_name='iso')),
            ],
            options={
                'verbose_name': 'PMActivityMaster',
                'verbose_name_plural': 'PMActivityMasters',
            },
        ),
        migrations.CreateModel(
            name='PMSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maint_ord', models.IntegerField(blank=True, default=100, null=True, verbose_name='Maint Ord')),
                ('schedule_due_date', models.DateField(verbose_name='Schedule Due Date')),
                ('schedule_class', models.CharField(blank=True, max_length=50, null=True, verbose_name='Schd Class')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipment.equipment', verbose_name='')),
            ],
            options={
                'verbose_name': 'PMSchedule',
                'verbose_name_plural': 'PMSchedules',
            },
        ),
        migrations.CreateModel(
            name='PMScheduleFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.BooleanField(default=False, verbose_name='Flag')),
                ('start_time', models.DateTimeField(verbose_name='Date of Beginning')),
                ('end_time', models.DateTimeField(verbose_name='Date of Ending')),
                ('spare_issued', models.TextField(verbose_name='Spare Issued')),
                ('remarks', models.TextField(verbose_name='Remarks')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preventive_maintenance.pmschedule', verbose_name='Schedule Id')),
            ],
            options={
                'verbose_name': 'PMScheduleFeedback',
                'verbose_name_plural': 'PMScheduleFeedbacks',
            },
        ),
        migrations.CreateModel(
            name='BreakDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(choices=[('Y', 'Y'), ('M', 'M'), ('N', 'N')], max_length=50, verbose_name='Flag')),
                ('break_down_date', models.DateTimeField(verbose_name='Break down Datetime')),
                ('fault_reported', models.CharField(max_length=500, verbose_name='Fault')),
                ('up_date_time', models.DateTimeField(verbose_name='Up datetime')),
                ('total_breakdown_hrs', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='breakdown hrs')),
                ('cause_code', models.CharField(blank=True, choices=[('M', 'M'), ('E', 'E')], max_length=500, null=True, verbose_name='cause_code')),
                ('reason', models.TextField(verbose_name='Reason')),
                ('description_of_mtc_activity_done', models.TextField(verbose_name='Description of Maintenance Activity Done')),
                ('fir_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.fircode', verbose_name='FIR')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipment.equipment', verbose_name='')),
            ],
            options={
                'verbose_name': 'BreakDown',
                'verbose_name_plural': 'BreakDowns',
            },
        ),
    ]
