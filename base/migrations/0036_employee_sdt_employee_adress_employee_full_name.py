# Generated by Django 4.0.2 on 2022-04-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_remove_customer_adress_customer_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='SDT',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='adress',
            field=models.ManyToManyField(blank=True, to='base.Address'),
        ),
        migrations.AddField(
            model_name='employee',
            name='full_name',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
