# Generated by Django 4.0.2 on 2022-04-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_rename_bookcategory_book_book_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_Category',
            new_name='book_category',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='number_Page',
            new_name='number_page',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publish_Date',
            new_name='publish_date',
        ),
        migrations.AlterField(
            model_name='book',
            name='height',
            field=models.FloatField(blank=True, help_text='cm', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='width',
            field=models.FloatField(blank=True, help_text='cm', null=True),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='pin',
            field=models.IntegerField(blank=True, default=None, help_text='mAh', null=True),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='ram',
            field=models.IntegerField(blank=True, default=None, help_text='GB', null=True),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='rom',
            field=models.IntegerField(blank=True, default=None, help_text='GB', null=True),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='screen_size',
            field=models.FloatField(blank=True, default=None, help_text='inch', null=True),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='weight',
            field=models.FloatField(blank=True, default=None, help_text='g', null=True),
        ),
    ]
