# Generated by Django 4.0.2 on 2022-03-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', null=True, upload_to=''),
        ),
    ]