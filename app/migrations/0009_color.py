# Generated by Django 4.2.3 on 2023-08-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_data_alter_product_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_code', models.CharField(max_length=100)),
            ],
        ),
    ]
