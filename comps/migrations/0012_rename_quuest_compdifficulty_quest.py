# Generated by Django 3.2.8 on 2021-10-20 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0011_compdifficulty_quuest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compdifficulty',
            old_name='quuest',
            new_name='quest',
        ),
    ]
