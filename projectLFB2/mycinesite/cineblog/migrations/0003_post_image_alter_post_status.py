# Generated by Django 5.1.5 on 2025-03-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineblog', '0002_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/bg.png', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Temporary')], default=1),
        ),
    ]
