# Generated by Django 4.2.5 on 2023-09-14 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apP', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contacts_name',
            new_name='contact_name',
        ),
    ]
