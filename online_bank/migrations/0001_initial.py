# Generated by Django 5.1 on 2024-10-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30)),
            ],
        ),
    ]
