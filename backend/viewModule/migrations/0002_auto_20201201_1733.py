# Generated by Django 3.1.3 on 2020-12-01 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['total']},
        ),
        migrations.AlterModelTable(
            name='tri',
            table='tt_tri_dump',
        ),
    ]
