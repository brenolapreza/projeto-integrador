from django.db import models
from pacientes.models import Paciente
from funcionarios.models import Medico

class Consulta(models.Model):
    nome = models.ForeignKey(Paciente, verbose_name="nome do paciente", on_delete=models.CASCADE, null=True, blank=True)
    nome_medico = models.ForeignKey(Medico, verbose_name="nome do médico", on_delete=models.CASCADE, null=True, blank=True)
    motivo = models.TextField("motivo da consulta", max_length=200, null=True, blank=True)
    data_consulta = models.DateTimeField("agendada para:", null=True, blank=True)

    def __str__(self):
        return self.nome.nome