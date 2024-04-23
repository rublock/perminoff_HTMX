from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('rosetta/', include('rosetta.urls')),
]

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('books.urls')),
)
