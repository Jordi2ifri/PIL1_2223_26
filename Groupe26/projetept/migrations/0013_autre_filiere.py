# Generated by Django 4.2.2 on 2023-06-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetept', '0012_rename_licences1_licences_delete_licences2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='autre',
            name='filiere',
            field=models.CharField(choices=[('IM', 'IM'), ('GL', 'GL'), ('SI', 'SI'), ('IA', 'IA'), ('SAOIT', 'SAOIT')], default='IM', max_length=20),
        ),
    ]
