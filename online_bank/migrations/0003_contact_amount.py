# Generated by Django 5.1 on 2024-10-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_bank', '0002_contact_acc_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
