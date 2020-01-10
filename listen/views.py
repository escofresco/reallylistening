from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .forms import EmptyForm
from .tasks import start_listening


class HomeView(TemplateView):
    template_name = "pages/home.html"
    form_class = EmptyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room_name"] = "test"
        return context

    def post(self, request, *args, **kwargs):
        if "file_url" in request.POST:
            # start a worker task for processing file located at file_url
            res = start_listening.apply_async(
                (request.POST["file_url"],), time_limit=60 * 20, soft_time_limit=60 * 15
            )
            return JsonResponse({"task_id": res.id})


class ListenedView(TemplateView):
    """Call pipeline with the task id passed by the url, then display results.
    """

    template_name = "pages/listened.html"

    def get(self, request, task_id):
        return render(request, self.template_name, {"task_id": task_id})

    def post(self, request, *args, **kwargs):
        if "task_id" in request.POST:
            async_res = start_listening.AsyncResult(request.POST["task_id"])

            if async_res.ready():
                return JsonResponse({"ready": True, "textcontent": async_res.get()})
            return JsonResponse({"ready": False})
