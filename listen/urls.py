from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView

urlpatterns = [
    # home page
    path("", HomeView.as_view(), name="home"),
    # about page
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
]
