# Generated by Django 4.0.2 on 2022-03-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='card_name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='exp_mon',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='exp_year',
        ),
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'PENDING')], default=2),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]