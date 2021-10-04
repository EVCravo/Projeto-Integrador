from django.db import models


class Paciente(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=50)
    cpf = models.DecimalField(max_digits=5, decimal_places=2)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


