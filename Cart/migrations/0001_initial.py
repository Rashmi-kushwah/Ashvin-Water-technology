# Generated by Django 5.0.2 on 2024-06-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('user_uid', models.CharField(blank=True, max_length=50, null=True)),
                ('sku_code', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('img1', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('qty', models.CharField(blank=True, max_length=20, null=True)),
                ('size', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('mrp', models.IntegerField(blank=True, null=True)),
                ('delivery_charges', models.CharField(blank=True, max_length=30, null=True)),
                ('discount', models.CharField(blank=True, max_length=30, null=True)),
                ('total_amount', models.CharField(blank=True, max_length=30, null=True)),
                ('total_qty', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
