from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View


class LoadTemplateView(View):
    
    main = ['cosmetics/index.html']
    #You put any code you may need here
    def get(self, request, *args, **kwargs):

        return render(request, self.main)