# Generated by Django 4.1.6 on 2023-02-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=300, null=True),
        ),
    ]