# Generated by Django 4.0.2 on 2022-04-17 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Phone',
            new_name='MobilePhone',
        ),
    ]
