# Generated by Django 4.2.2 on 2023-06-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetept', '0014_licences_semestres'),
    ]

    operations = [
        migrations.DeleteModel(
            name='autre',
        ),
        migrations.AddField(
            model_name='licences',
            name='Notification',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
