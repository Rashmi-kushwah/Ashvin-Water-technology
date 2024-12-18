# Generated by Django 5.0.2 on 2024-06-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_img1', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title1_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title1_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img2', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title2_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title2_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img3', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title3_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title3_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img4', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title4_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title4_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img5', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title5_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title5_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img6', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title6_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title6_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img7', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title7_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title7_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img8', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title8_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title8_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img9', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title9_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title9_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img10', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title10_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title10_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img11', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title11_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title11_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img12', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title12_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title12_p', models.CharField(blank=True, max_length=500, null=True)),
                ('bg_img13', models.ImageField(blank=True, max_length=200, null=True, upload_to='photos/')),
                ('title13_h3', models.CharField(blank=True, max_length=500, null=True)),
                ('title13_p', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
