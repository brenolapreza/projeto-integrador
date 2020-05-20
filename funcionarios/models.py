from django.db import models

class Medico(models.Model):
    nome = models.CharField("nome", max_length=64, null=True, blank=True)
    crm = models.CharField("CRM", max_length=64, null=True, blank=True)
    especialidade = models.CharField("especialidade", max_length=64, null=True, blank=True)

    def __str__(self):
        return self.nome


