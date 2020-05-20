from django.db import models
from pacientes.models import Paciente
from consultas.models import Consulta
#tipo de exame
URINA = 1
SANGUE = 2
VISTA = 3
MAMOGRAFIA = 4
TOMOGRAFIA = 5
ROTINA = 6
PEZINHO = 7

TIPO_EXAME = [
    (1, 'Urina'),
    (2, 'Sangue'),
    (3, 'Vista'),
    (4, 'Mamografia'),
    (5, 'Tomografia'),
    (6, 'Rotina'),
    (7, 'Pezinho'),

]
#Urgencia do Exame
LEVE = 1
GRAVE = 2
GRAVISSIMO = 3

GRAU_EXAME = [
    (1, 'Leve'),
    (2, 'Grave'),
    (3, 'Gravissimo'),
]
#Diagnostico
SAUDAVEL = 1
MEDIO = 2
DOENTE = 3

DIAGNOSTICO_EXAME = [
    (1, 'Saudavel'),
    (2, 'Medio'),
    (1, 'Doente'),
]

class Exame(models.Model):
    exame_paciente = models.ForeignKey(Paciente, verbose_name="nome do paciente", on_delete=models.CASCADE, null=True, blank=True)
    _tipo = models.PositiveIntegerField("tipo de exame", choices=TIPO_EXAME, default=SANGUE)
    _grau = models.PositiveIntegerField("Grau do Exame", choices=GRAU_EXAME, default=LEVE)

    def __str__(self):
        return str(self.exame_paciente.nome)

    #tipo de exame
    @property
    def tipo(self):
        for code, label in TIPO_EXAME:
            if self._tipo == code:
                break
        return label

    @tipo.setter
    def tipo(self, valor):
        if valor == 'Urina':
            self._tipo = URINA
        elif valor == 'Sangue':
            self._tipo = SANGUE
        elif valor == 'Vista':
            self._tipo = VISTA
        else:
            raise ValueError('Escola entre: Urina, Sangue ou Vista')
    #Urgencia do exame
    @property
    def grau(self):
        for code, label in GRAU_EXAME:
            if self._tipo == code:
                break
        return label

    @grau.setter
    def grau(self, valor):
        if valor == 'Leve':
            self._grau = LEVE
        elif valor == 'Grave':
            self._grau = GRAVE
        elif valor == 'Gravissimo':
            self._grau = GRAVISSIMO
        else:
            raise ValueError('Escola entre: Leve, Grave ou Gravissimo')
        

    
  