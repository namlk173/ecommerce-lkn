# Generated by Django 4.0.2 on 2022-05-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_alter_orderproduct_options_alter_address_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='SDT',
            new_name='phone_number',
        ),
        migrations.AddField(
            model_name='address',
            name='phone_number_receiver',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='receiver',
            field=models.TextField(max_length=100, null=True),
        ),
    ]