from django.db import models
from cloudinary.models import CloudinaryField
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

# Create your models here.


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    enderecos = models.ForeignKey(Endereco, models.CASCADE, null=True, blank=True)
    foto = CloudinaryField('foto')

    def __str__(self):
        return self.nome
