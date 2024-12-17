# Generated by Django 2.0 on 2024-12-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0002_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='log',
        ),
        migrations.AddField(
            model_name='log',
            name='vehicle',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fuel.Vehicle'),
        ),
    ]
