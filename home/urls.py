"""URLs for Home App."""

from django.urls import path

from home.views import IndexTemplateView, PageDetailView

app_name = "home"

urlpatterns = [
    path(
        "",
        IndexTemplateView.as_view(),
        name="index",
    ),
    path(
        "company/<str:key>/",
        PageDetailView.as_view(),
        name="page_detail",
    ),
]
