# Generated by Django 4.2.5 on 2023-09-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apP', '0002_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=60, null=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category/')),
            ],
        ),
    ]
