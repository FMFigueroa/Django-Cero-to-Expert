# Generated by Django 3.2.4 on 2021-07-07 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_producto_imagen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marca',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='marca',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nuevo',
            new_name='disponible',
        ),
    ]
