from django.shortcuts import render
#
from django.views.generic import TemplateView
#

# Create your views here.


class IndexView(TemplateView):
    template_name = 'home/index.html'
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user_login'] = self.request.user
        return context
    
    