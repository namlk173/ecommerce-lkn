# Generated by Django 4.0.2 on 2022-04-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_alter_cart_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
