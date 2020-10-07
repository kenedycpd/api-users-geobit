from django.db import models


class Users(models.Model):
    username = models.CharField('Usuario', max_length=100, blank=False)
    email = models.CharField('E-mail', max_length=100, blank=False)
    password = models.CharField('Senha', max_length=100, blank=False)

    def __str__(self):
        return self.username
