# Generated by Django 2.1.5 on 2019-03-23 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_contact_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
    ]