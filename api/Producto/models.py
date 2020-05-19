from django.db import models


class Producto(models.Model):

    tipo_producto = (
        ('dif', 'Difusor'),
        ('tex', 'Textil'),
        ('aut', 'Auto'),
        ('ace', 'Aceite'),
        ('mas', 'Mascota'),
        ('ant', 'Antibacterial')
    )

    linea_producto = (
        ('nam', 'Namaste'),
        ('coc', 'Coconut'),
        ('pos', 'Positive'),
        ('tea', 'Tea Leaves'),
        ('spa', 'Spa'),
        ('sof', 'Soft')
    )
    tipo = models.CharField(max_length=1, choices=tipo_producto)
    linea = models.CharField(max_length=1, choices=linea_producto)
    aroma = models.CharField(max_length=30)
    precio = models.IntegerField(max_length=10)
