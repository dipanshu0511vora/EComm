# Generated by Django 5.0.3 on 2024-05-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "products",
            "0002_colorvariant_sizevariant_alter_productimage_product_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="color_variant",
            field=models.ManyToManyField(blank=True, to="products.colorvariant"),
        ),
        migrations.AlterField(
            model_name="product",
            name="size_variant",
            field=models.ManyToManyField(blank=True, to="products.sizevariant"),
        ),
    ]
