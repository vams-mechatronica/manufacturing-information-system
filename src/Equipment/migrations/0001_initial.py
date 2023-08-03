# Generated by Django 4.2.4 on 2023-08-02 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0001_initial'),
        ('Suppliers', '0001_initial'),
        ('Manufacturer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Equipemnt Number')),
                ('description', models.CharField(max_length=350, verbose_name='Description')),
                ('short_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Short Name')),
                ('bay', models.CharField(max_length=50, verbose_name='Bay')),
                ('column', models.CharField(max_length=50, verbose_name='Column')),
                ('section', models.CharField(max_length=50, verbose_name='Section')),
                ('section_eln', models.CharField(max_length=50, verbose_name='Section ELN')),
                ('equipment_type', models.CharField(max_length=50, verbose_name='Equipment Type')),
                ('sr_number', models.CharField(max_length=50, verbose_name='M/C Sr. No. Alloted by Mfg.')),
                ('model_number', models.CharField(max_length=50, verbose_name='M/C Model Number')),
                ('indian_agent', models.BooleanField(verbose_name='Indian Agent')),
                ('make', models.CharField(max_length=50, verbose_name='Make')),
                ('cost', models.CharField(max_length=50, verbose_name='Cost')),
                ('cost_in_lakhs', models.CharField(max_length=50, verbose_name='Cost in Lakhs')),
                ('po_number', models.CharField(max_length=50, verbose_name='PO Number')),
                ('po_date', models.DateField(verbose_name='PO Date')),
                ('ptc_issue_date', models.DateField(verbose_name='PTC Issue Date')),
                ('warranty', models.CharField(max_length=50, verbose_name='Warranty(from the date of commissioning and proving out of MnP)')),
                ('amc_covered_in_po', models.BooleanField(verbose_name='AMC covered in PO')),
                ('amc_type', models.CharField(max_length=50, verbose_name='Type of AMC')),
                ('amc_validity', models.DateField(verbose_name='Validity of AMC')),
                ('recovery_value_warranty', models.CharField(max_length=50, verbose_name='Recovery Value in Warranty Period')),
                ('percentage_avalability_in_warranty', models.CharField(max_length=50, verbose_name='%age Availability in Warranty Period')),
                ('specification', models.TextField(max_length=5000, verbose_name='Specifications')),
                ('machine_image', models.BinaryField(blank=True, editable=True, null=True, verbose_name='machine_image')),
                ('po_copy', models.BinaryField(blank=True, editable=True, null=True, verbose_name='po_copy_image')),
                ('manufacturer_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manufacturer.manufacturer', verbose_name='Manufacturer Code')),
                ('shop_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.shop', verbose_name='Shop Number')),
                ('supplier_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Suppliers.supplier', verbose_name='Supplier Code')),
            ],
            options={
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipments',
            },
        ),
    ]
