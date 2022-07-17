# Generated by Django 4.0.5 on 2022-07-17 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shades', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mens_Eye_Glasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mens_Sun_Glasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Womens_Eye_Glasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Womens_Sun_Glasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Blue_Ray_Glasses',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shades.mens_eye_glasses'),
        ),
    ]
