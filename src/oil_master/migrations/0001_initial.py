# Generated by Django 4.2.4 on 2024-05-26 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OilMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pl_no', models.CharField(max_length=50, verbose_name='PL No.')),
                ('flag', models.CharField(blank=True, max_length=50, null=True, verbose_name='Flag')),
                ('date', models.DateField(verbose_name='date')),
                ('qty_received', models.IntegerField(verbose_name='Quantity Received')),
                ('qty_issued', models.IntegerField(verbose_name='Quantity Issued')),
                ('meter_reading', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Meter Read')),
                ('unit', models.IntegerField(verbose_name='Unit')),
                ('remarks', models.TextField(verbose_name='Remarks')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipment.equipment', verbose_name='Machine')),
            ],
            options={
                'verbose_name': 'OilMaster',
                'verbose_name_plural': 'OilMasters',
            },
        ),
    ]
