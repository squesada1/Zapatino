# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='detalle_producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True)),
                ('descipcion', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField(null=True)),
                ('direccion', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('codigo_postal', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=30)),
                ('fecha_ingreso', models.DateField(null=True)),
                ('precio_costo', models.FloatField(null=True)),
                ('precio_publico', models.FloatField(null=True)),
                ('stock_minimo', models.IntegerField(null=True)),
                ('stock_maximo', models.IntegerField(null=True)),
                ('categoria', models.ForeignKey(to='zapatino_shop.categoria', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='provincia',
            fields=[
                ('nombre', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('ciudad', models.ManyToManyField(to='zapatino_shop.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='tallenumero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tallenumero_desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='zapatino_shop.persona')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.IntegerField(null=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
            ],
            bases=('zapatino_shop.persona',),
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='zapatino_shop.persona')),
                ('razon_social', models.CharField(max_length=30)),
                ('cuit', models.CharField(max_length=30)),
                ('cbu', models.CharField(max_length=30)),
                ('ncuenta', models.CharField(max_length=30)),
                ('contacto', models.CharField(max_length=50)),
                ('marca', models.ForeignKey(to='zapatino_shop.marca')),
            ],
            bases=('zapatino_shop.persona',),
        ),
        migrations.AddField(
            model_name='detalle_producto',
            name='producto',
            field=models.ForeignKey(to='zapatino_shop.producto', db_column=b'producto_id'),
        ),
        migrations.AddField(
            model_name='detalle_producto',
            name='tallenumero',
            field=models.ForeignKey(to='zapatino_shop.tallenumero', db_column=b'tallenumero_id'),
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(to='zapatino_shop.proveedor', null=True),
        ),
    ]
