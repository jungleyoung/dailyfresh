# Generated by Django 2.2.4 on 2019-08-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyfresh', '0002_auto_20190807_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddr',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default=' ', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upocode',
            field=models.CharField(default=' ', max_length=6),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='urer',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
