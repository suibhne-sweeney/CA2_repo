# Generated by Django 4.1.3 on 2022-12-03 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_category_alter_package_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='category',
        ),
    ]