# Generated by Django 5.0.2 on 2024-06-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('user_uid', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('house_no', models.CharField(blank=True, max_length=10, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('street1', models.CharField(blank=True, max_length=100, null=True)),
                ('street2', models.CharField(blank=True, max_length=100, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(default='India', max_length=50)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('order_date', models.CharField(blank=True, max_length=100, null=True)),
                ('tracking_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tracking_link', models.CharField(blank=True, max_length=100, null=True)),
                ('order_status', models.CharField(blank=True, max_length=100, null=True)),
                ('total_amount', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('qty', models.CharField(blank=True, max_length=30, null=True)),
                ('img1', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
            ],
        ),
    ]
