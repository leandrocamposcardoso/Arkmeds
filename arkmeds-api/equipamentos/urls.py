
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register('empresa', views.EmpresaView, basename='empresa')
router.register('equipamento', views.EquipamentoView, basename='equipamento')
router.register('proprietario', views.ProprietarioView, basename='proprietario')
router.register('tipo_equipamento', views.TipoEquipamentoView, basename='tipo_equipamento')
router.register('responsavel_tecnico', views.ResponsavelTecnicoView, basename='responsavel_tecnico')
router.register('chamado_equipamento', views.ChamadoEquipamentoView, basename='chamado_equipamento')
urlpatterns = format_suffix_patterns(router.urls)
