# Generated by Django 5.0.3 on 2024-03-18 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_remove_networkobject_products_product_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='supplier',
            new_name='suppliers',
        ),
    ]
