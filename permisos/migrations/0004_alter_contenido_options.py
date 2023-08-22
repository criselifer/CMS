# Generated by Django 4.2.4 on 2023-08-22 03:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("permisos", "0003_alter_contenido_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contenido",
            options={
                "permissions": (
                    ("crear_contenido", "Crear contenido"),
                    ("editar_contenido", "Editar contenido"),
                    ("publicar_contenido", "Publicar contenido"),
                )
            },
        ),
    ]