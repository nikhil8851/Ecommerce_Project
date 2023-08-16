# Generated by Django 4.2.2 on 2023-07-17 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='main_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sub_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cat')),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='main_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.main_cat'),
        ),
    ]
