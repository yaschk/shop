# Generated by Django 2.1.7 on 2019-02-28 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascord', '0002_auto_20190228_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
    ]
