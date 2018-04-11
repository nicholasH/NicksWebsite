from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from .models import businessCard
from django.shortcuts import render




def home(request):
    template_name = 'homepage/porfolio.html'

    return render(request,template_name)

class homeView(generic.DetailView):
    template_name = 'homepage/porfolio.html'
    model = businessCard

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return