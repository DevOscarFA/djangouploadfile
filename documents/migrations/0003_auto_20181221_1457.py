# Generated by Django 2.1.4 on 2018-12-21 19:57

from django.db import migrations, models
import documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20181221_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attach',
            name='externalURL',
        ),
        migrations.AlterField(
            model_name='attach',
            name='image',
            field=models.FileField(upload_to='', validators=[documents.models.upload_pdf_validator], verbose_name=documents.models.PathAndRename('images/uploads/2018/12/21')),
        ),
    ]