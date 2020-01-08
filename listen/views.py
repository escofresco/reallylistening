from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signature"] = "issasignature"
        return context
