# Generated by Django 4.1.3 on 2022-11-30 02:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_location_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('hotel', models.CharField(max_length=100)),
                ('tour', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='locations')),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
