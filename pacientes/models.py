from django.db import models


CRIANCA = 1
JOVEM = 2
ADULTO = 3
IDOSO = 4

IDADE_PACIENTE = [
    (1, 'Criança'),
    (2, 'Jovem'),
    (3, 'Adulto'),
    (4, 'Idoso'),
]

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField("nome", max_length=50, null=True, blank=True)
    cpf = models.CharField("cpf", unique=True, db_index=True, max_length=15, null=True)
    telefone = models.CharField("telefone", max_length=50, null=True, blank=True)
    endereco = models.CharField("endereço", max_length=60, null=True, blank=True)
    idade = models.PositiveIntegerField("Idade Pessoa", choices=IDADE_PACIENTE, default=CRIANCA)
    nacionalidade = models.CharField("nascionalidade", max_length=60, null=True, blank=True)
    diagnostico = models.TextField("Diagnóstico", max_length=500, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    editado_em = models.DateTimeField("Última visualização", auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nome

class Especial(Paciente):
    is_especial = models.BooleanField("especial", default=True)
    info_especial = models.TextField("Informações Especial", max_length=500, null=True, blank=True)
    
    

    def __str__(self):
        return super().__str__() + ' - especial: ' + str(self.is_especial)