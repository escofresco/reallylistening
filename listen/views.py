from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .forms import EmptyForm
from .tasks import add


class HomeView(TemplateView):
    template_name = 'pages/home.html'
    form_class = EmptyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_name'] = 'test'
        return context

    def post(self, request, *args, **kwargs):
        if 'file_url' in request.POST:
            res = add.apply_async((2,2))
            return JsonResponse({'task_id': res.id})

class ListenedView(TemplateView):
    '''Call pipeline with the task id passed by the url, then display results.
    '''
    template_name = 'pages/listened.html'

    def get(self, request, task_id):
        return render(request, self.template_name, {'task_id': task_id})

    def post(self, request, *args, **kwargs):
        if 'task_id' in request.POST:
            async_res = add.AsyncResult(request.POST['task_id'])

            if async_res.ready():
                return JsonResponse({'ready': True, 'res': async_res.get()})
            return JsonResponse({'ready': False})
