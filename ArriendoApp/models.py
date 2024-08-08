from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoPropiedad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):

    calle = models.CharField(max_length=50, blank=False,null=False)
    numero = models.IntegerField()
    departamento = models.CharField(max_length=10)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.calle} {self.numero} {self.departamento} {self.comuna} {self.comuna.region}'
    
class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo, password, **extra_fields)

class Usuario(AbstractBaseUser):
    nombres = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True, blank=True)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    correo = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombres', 'rut', 'telefono', 'tipo_usuario']

    def __str__(self):
        return self.correo

class Propiedad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    garantia = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_propiedad = models.ForeignKey(TipoPropiedad, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
