# Generated by Django 2.1.4 on 2020-07-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(default=1, upload_to='videos/'),
        ),
    ]
