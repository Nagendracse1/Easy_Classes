# Generated by Django 3.0.5 on 2020-04-11 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about_swlp_icons',
            old_name='about',
            new_name='section',
        ),
    ]