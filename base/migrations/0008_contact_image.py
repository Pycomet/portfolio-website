# Generated by Django 2.1.5 on 2019-03-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pictures'),
        ),
    ]