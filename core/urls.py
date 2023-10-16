"""URLs for the core app."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("products/", include("products.urls")),
    path("cart/", include("cart.urls")),
]

# path('users/', include('users.urls')),

# Debug Config
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)


# Custom attributes for admin
admin.site.site_header = "New Store"
admin.site.site_title = "New Store"
admin.site.index_title = "Admin"
