from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    permission_classes = [IsAuthenticated,]
    search_fields = ('nome', 'descricao', 'enderecos__linha1')
    lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id')
        nome = self.request.query_params.get('nome')
        descricao = self.request.query_params.get('descricao')

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome=nome)

        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post'], detail=True)
    def denunciar(self, request, pk=None):
        """
        action própria
        urls /caminho/pk/nome_da_action
        action pra um recurso
        """
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        """
        Action para todos os elementos (sem pk a.k.a list)
        :param request:
        :return:
        """
        pass
