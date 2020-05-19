from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField("nome", max_length=50, null=True, blank=True)
    cpf = models.CharField("cpf", unique=True, db_index=True, max_length=15, null=True)
    data_nascimento = models.DateField("Data de nascimento", null=True, blank=True)
    telefone = models.CharField("telefone", max_length=50, null=True, blank=True)
    endereco = models.CharField("endereço", max_length=60, null=True, blank=True)
    nascionalidade = models.CharField("nascionalidade", max_length=60, null=True, blank=True)
    diagnostico = models.TextField("Diagnóstico", max_length=500, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    editado_em = models.DateTimeField("Última visualização", auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nome

