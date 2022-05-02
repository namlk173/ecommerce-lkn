# Generated by Django 4.0.2 on 2022-05-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_alter_order_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='order',
        ),
        migrations.AddField(
            model_name='checkout',
            name='order_Items',
            field=models.ManyToManyField(blank=True, to='base.OrderProduct'),
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]
