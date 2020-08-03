from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from analytics.models import ClickEvent

from .models import RezseclyURL
from .forms import RezForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = RezForm()
        context = {"form": form}
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = RezForm(request.POST)
        context = {"form": form}
        template = "shortener/home.html"

        if form.is_valid():
            submited_url = form.cleaned_data.get('url')
            obj, created = RezseclyURL.objects.get_or_create(url=submited_url)
            context = {
                "object":obj,
                "created":created,
            }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already-exists.html'

        return render(request, template, context)

class RezRedirectCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(RezseclyURL, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
