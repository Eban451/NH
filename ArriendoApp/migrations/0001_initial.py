# Generated by Django 3.2.7 on 2024-08-07 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('departamento', models.CharField(max_length=10)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArriendoApp.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombres', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('direccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArriendoApp.direccion')),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArriendoApp.tipousuario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('m2_construidos', models.FloatField()),
                ('m2_totales', models.FloatField()),
                ('estacionamientos', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
                ('banos', models.IntegerField()),
                ('precio_arriendo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('garantia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponible', models.BooleanField(default=True)),
                ('arrendador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArriendoApp.usuario')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArriendoApp.comuna')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArriendoApp.direccion')),
                ('tipo_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_inmueble', to='ArriendoApp.tipopropiedad')),
                ('tipo_propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArriendoApp.tipopropiedad')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArriendoApp.region'),
        ),
    ]
