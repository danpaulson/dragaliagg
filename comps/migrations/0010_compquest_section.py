# Generated by Django 3.2.8 on 2021-10-20 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0009_compdifficulty_compquest'),
    ]

    operations = [
        migrations.AddField(
            model_name='compquest',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='quests', to='comps.compsection'),
        ),
    ]
