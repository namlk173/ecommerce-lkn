# Generated by Django 4.0.2 on 2022-05-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_rename_product_comment_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='payment_or_shipping',
            field=models.TextField(choices=[('payment', 'payment'), ('shipping', 'shipping')], default='shipping', max_length=50),
        ),
    ]
