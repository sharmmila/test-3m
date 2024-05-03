from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from film.views import main_view, list_films_view, film_detail_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view),
    path("films/", list_films_view),
    path("films/<int:film_id>/", film_detail_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
