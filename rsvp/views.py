from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from rsvp import forms


class Home(TemplateView):

    template_name = 'rsvp/home.html'


class Info(TemplateView):

    template_name = 'rsvp/info.html'


class ResponseCreate(CreateView):

    form_class = forms.ResponseForm
    template_name = 'rsvp/response_form.html'
    success_url = reverse_lazy('response-done')


class ResponseDone(TemplateView):

    template_name = 'rsvp/response_done.html'


class Registry(TemplateView):

    template_name = 'rsvp/registry.html'
