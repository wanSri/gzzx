from django.conf.urls import url
from django.urls import include
from zx.views import uploadConfigFile
from rest_framework import routers
from .views import EquViewSet, ZhuanLineListView, ZhuanLineDetail, EqupmentListView, EquipDetailView \
    , generateTable, EapiListView, LoboListView, exportblo, exporteapi

router = routers.SimpleRouter()
router.register(r'equ', EquViewSet, base_name='equ')

app_name = 'zx'
urlpatterns = [
    url('uploadConfigFile/', uploadConfigFile, name='uploadConfigFile'),
    url('', include(router.urls)),
    url('^zl/$', ZhuanLineListView.as_view()),
    url('^zl/(?P<pk>\d+)/$', ZhuanLineDetail.as_view()),
    url('^equip/$', EqupmentListView.as_view()),
    url('^equip/(?P<pk>\d+)/$', EquipDetailView.as_view()),
    url('^generateTable/', generateTable),
    url('^eapi/$', EapiListView.as_view()),
    url('^lobo/$', LoboListView.as_view()),
    url('^exportblo/(?P<start>\d+)/(?P<limit>\d+)/$', exportblo),
    url('^exporteapi/(?P<start>\d+)/(?P<limit>\d+)/$', exporteapi),
]
