# Generated by Django 2.1.5 on 2019-02-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mentor', '0002_auto_20190213_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='Foto',
            field=models.FileField(null=True, upload_to='Mentor/', verbose_name=''),
        ),
    ]
