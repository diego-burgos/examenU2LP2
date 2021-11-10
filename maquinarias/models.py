from django.db import models

# Create your models here.

class Maquinaria(models.Model):

    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    nr_serie=models.CharField(max_length=50)
    tp_combustible=models.CharField(max_length=50)
    tp_maquinaria=models.CharField(max_length=50)
    placa=models.CharField(max_length=50)
    conductor=models.ForeignKey("Conductor", on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Maquinaria")
        verbose_name_plural = ("Maquinarias")

    def __str__(self):
        return self.marca

class Conductor(models.Model):

    nombres=models.CharField(max_length=50)
    apellidoPT=models.CharField(max_length=50)
    apellidoMT=models.CharField(max_length=50)
    dni=models.CharField(max_length=50)
    celular=models.CharField(max_length=50)
    tp_licencia=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = ("Conductor")
        verbose_name_plural = ("Conductors")

    def __str__(self):
        return self.nombres
