from django.db import models
from pacientes.models import Paciente
from consultas.models import Consulta
#tipo de exame

URINA = 1
SANGUE = 2
VISTA = 3

TIPO_EXAME = [
    (1, 'Urina'),
    (2, 'Sangue'),
    (3, 'Vista'),
]

class Exame(models.Model):
    exame_paciente = models.ForeignKey(Paciente, verbose_name="nome do paciente", on_delete=models.CASCADE, null=True, blank=True)
    _tipo = models.PositiveIntegerField("tipo de exame", choices=TIPO_EXAME, default=SANGUE)
    data_entrega = models.DateTimeField("data de entrega", null=True, blank=True)

    def __str__(self):
        return self.exame_paciente.nome