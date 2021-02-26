from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings
from django.contrib.auth import get_user_model  # maneira recomendada


class Post(models.Model):
    # autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    # autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)  # maneira recomendada
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self) -> models.CharField:
        return self.titulo
