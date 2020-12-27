from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import debug_toolbar
#from django.contrib.flatpages import views
from django.urls import include, path
#from django.conf.urls import handler404, handler500

#handler404 = 'posts.views.page_not_found'
#handler500 = 'posts.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('about/', include('django.contrib.flatpages.urls')),
#    path('auth/', include('users.urls')),
#    path('auth/', include('django.contrib.auth.urls')),
    path('oil-statistic/', include('oil_stats.urls')),
]
'''
urlpatterns += [
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
    path('terms/', views.flatpage, {'url': '/terms/'}, name='terms'),
    path('about-spec/', views.flatpage, {'url': '/about-spec/'}, name='spec'),
    path('about-author/', views.flatpage, {'url': '/about-author/'}, name='author'),
]
'''
if settings.DEBUG:
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
