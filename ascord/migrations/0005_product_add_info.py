# Generated by Django 2.1.7 on 2019-02-28 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascord', '0004_auto_20190228_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='add_info',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]
