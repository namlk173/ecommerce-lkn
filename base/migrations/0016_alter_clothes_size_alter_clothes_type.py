# Generated by Django 4.0.2 on 2022-04-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_clothes_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='type',
            field=models.TextField(blank=True, null=True),
        ),
    ]
