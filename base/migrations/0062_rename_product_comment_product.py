# Generated by Django 4.0.2 on 2022-05-15 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0061_alter_checkout_options_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Product',
            new_name='product',
        ),
    ]