from django.db import models
from django.contrib.auth import get_user_model


class Perfil(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    telefono = models.CharField(max_length=25)
    domicilio = models.CharField(max_length=100)
    referencia = models.TextField(blank=True, help_text='Cómo nos conociste?')

    def __str__(self):
        return 'Perfil del usuario: %s' % self.usuario.get_full_name()
