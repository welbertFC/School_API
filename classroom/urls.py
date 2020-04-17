from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import AlunoViewSet, ProfessorViewSet

router = SimpleRouter()
router.register('professor', ProfessorViewSet)
router.register('aluno', AlunoViewSet)

urlpatterns = [
    #path('professor/<int:professor_pk>/alunos/', ProfessorViewSet.as_view({'get': 'list'}), name='professor_alunos'),
]
