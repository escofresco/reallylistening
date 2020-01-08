from django.urls import path

from .views import HomeView
urlpatterns = [
    # home page
    path("", HomeView.as_view(), name="home"),

]
