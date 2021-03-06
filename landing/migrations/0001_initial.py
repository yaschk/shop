# Generated by Django 2.1.1 on 2018-10-31 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'My Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
    ]
