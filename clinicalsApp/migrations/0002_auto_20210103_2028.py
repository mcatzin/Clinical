# Generated by Django 3.1.4 on 2021-01-03 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinicaldata',
            old_name='patient',
            new_name='model',
        ),
    ]