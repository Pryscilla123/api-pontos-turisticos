from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco')

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)