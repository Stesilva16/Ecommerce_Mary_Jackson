# Generated by Django 4.2.11 on 2024-04-11 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_MJ", "0007_remove_cliente_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carrinhoproduto",
            name="avaliacao",
        ),
        migrations.RemoveField(
            model_name="carrinhoproduto",
            name="subtotal",
        ),
        migrations.AlterField(
            model_name="carrinho",
            name="cliente",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_MJ.cliente",
            ),
        ),
        migrations.DeleteModel(
            name="Pedido_order",
        ),
    ]
