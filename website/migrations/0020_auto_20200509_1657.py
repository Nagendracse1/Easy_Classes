# Generated by Django 3.0.5 on 2020-05-09 11:27

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20200508_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='summary',
        ),
        migrations.AddField(
            model_name='donate',
            name='bank_info',
            field=djrichtextfield.models.RichTextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='programs',
            name='image',
            field=models.ImageField(upload_to='images/programs/'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100, unique=True),
        ),
    ]
