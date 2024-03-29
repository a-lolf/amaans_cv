# Generated by Django 4.2.3 on 2023-07-21 21:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('email', models.EmailField(help_text='Please enter a valid email address.', max_length=254, validators=[django.core.validators.EmailValidator])),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
