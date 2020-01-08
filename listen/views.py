from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .forms import EmptyForm
from .tasks import add

class HomeView(TemplateView):
    template_name = "pages/home.html"
    form_class = EmptyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signature"] = "issasignature"
        return context

    def post(self, request, *args, **kwargs):
        add.apply_async((2, 2))
        return JsonResponse({"foo": "bar"})
