# Generated by Django 4.0.5 on 2022-11-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_autor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editora',
            name='site',
            field=models.URLField(null=True),
        ),
    ]
