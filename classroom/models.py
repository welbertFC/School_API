from django.db import models


class Base(models.Model):
    datetime_create = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Professor(Base):
    nome = models.CharField(max_length=300)
    datanasc = models.DateField()
    email = models.EmailField()

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
        unique_together = ['email']
        ordering = ['id']

    def __str__(self):
        return self.nome


class Aluno(Base):
    professor = models.ForeignKey(Professor,  related_name='alunos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=300)
    datanasc = models.DateField()
    serie = models.CharField(max_length=30)
    escola = models.TextField()
    observacao = models.TextField(blank=True, default='')


    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'
        ordering = ['id']


    def __str__(self):
        return self.professor
