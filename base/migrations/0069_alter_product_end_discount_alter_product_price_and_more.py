# Generated by Django 4.0.2 on 2022-05-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0068_product_discount_product_end_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_discount',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_discount',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
    ]
