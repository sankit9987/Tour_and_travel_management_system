# Generated by Django 4.0.2 on 2022-03-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('msg', models.CharField(max_length=100)),
            ],
        ),
    ]
