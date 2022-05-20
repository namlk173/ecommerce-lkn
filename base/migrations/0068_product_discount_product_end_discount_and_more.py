# Generated by Django 4.0.2 on 2022-05-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0067_alter_book_publish_date_alter_user_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=0, help_text='%'),
        ),
        migrations.AddField(
            model_name='product',
            name='end_discount',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='start_discount',
            field=models.DateField(blank=True, null=True),
        ),
    ]