# Generated by Django 4.1.1 on 2023-02-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_cat',
            field=models.CharField(default='', max_length=20),
        ),
    ]