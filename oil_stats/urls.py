from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='oil_index'),
#    path('pumps/', views.pump_list, name='pump_site'),
    path('pumps/', views.PumpListView.as_view(), name='pump_site'),
    path('add-pump/', views.add_pump, name='add_pump'),
    path('add-util/', views.add_util, name='add_util'),
    path('add-strainer-change/', views.add_strainer_change, name='add_strainer_change'),
#    path(r'^search/$', PumpView.as_view(filterset_class=FilmFilter, template_name='myapp/my_template.html'), name='searcher'),
]
