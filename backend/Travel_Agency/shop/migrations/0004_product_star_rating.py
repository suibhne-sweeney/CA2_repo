# Generated by Django 4.1.3 on 2022-12-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]