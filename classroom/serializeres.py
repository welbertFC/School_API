from rest_framework import serializers
from .models import Aluno, Professor


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = (
            'id',
            'professor',
            'nome',
            'datanasc',
            'serie',
            'escola',
            'observacao',
            'datetime_create'
        )


class ProfessorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Professor
        fields = (
            'id',
            'nome',
            'datanasc',
            'email',
            'datetime_create'
        )






