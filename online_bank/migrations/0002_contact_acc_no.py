# Generated by Django 5.1 on 2024-10-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='acc_no',
            field=models.IntegerField(default=10000000),
        ),
    ]
