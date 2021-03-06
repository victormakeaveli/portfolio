# Generated by Django 3.1.7 on 2021-03-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='null', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='relation',
            field=models.URLField(default='null'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projects',
            name='summary',
            field=models.TextField(),
        ),
    ]
