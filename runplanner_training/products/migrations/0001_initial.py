# Generated by Django 5.1.3 on 2024-11-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('training_plan', 'Training Plan'), ('nutrition', 'Nutrition')], default='training_plan', max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(unique=True)),
                ('order_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('distance', models.CharField(blank=True, choices=[('5k', '5k'), ('10k', '10k'), ('half_marathon', 'Half Marathon'), ('marathon', 'Marathon'), ('50k', '50k'), ('80k', '80k'), ('100k', '100k'), ('160k', '160k'), ('200k', '200k')], max_length=20, null=True)),
                ('difficulty', models.CharField(blank=True, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20, null=True)),
                ('terrain', models.CharField(blank=True, choices=[('road', 'Road'), ('trail', 'Trail'), ('mixed', 'Mixed')], max_length=20, null=True)),
                ('elevation', models.CharField(choices=[('0-500m', '0-500m'), ('500-1000m', '500-1000m'), ('1000-1500m', '1000-1500m'), ('1500-2000m', '1500-2000m'), ('2000-2500m', '2000-2500m'), ('2500-3000m', '2500-3000m'), ('3000-3500m', '3000-3500m'), ('3500-4000m', '3500-4000m'), ('4000-4500m', '4000-4500m'), ('4500-5000m', '4500-5000m'), ('5000-5500m', '5000-5500m'), ('5500-6000m', '5500-6000m'), ('6000-6500m', '6000-6500m'), ('6500-7000m', '6500-7000m'), ('7000-7500m', '7500-8000m'), ('8000-8500m', '8000-8500m'), ('8500-9000m', '8500-9000m'), ('9000-9500m', '9000-9500m'), ('9500-10000m', '9500-10000m')], max_length=20)),
            ],
        ),
    ]
