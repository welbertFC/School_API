from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Aluno, Professor

from .models import Aluno, Professor
from .serializeres import AlunoSerializer, ProfessorSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    @action(detail=True, methods=['get'])
    def alunos(self, request,pk=None):
        alunos = Aluno.objects.filter(professor_id=pk)
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)





class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer




    # def get_object(self):
    #     if self.kwargs.get('professor_pk'):
    #         return self.queryset.filter(professor_id=self.kwargs.get('professor_pk'))


