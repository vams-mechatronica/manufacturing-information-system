# Generated by Django 4.2.4 on 2024-05-28 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Equipment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='machine_image',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='po_copy',
        ),
    ]