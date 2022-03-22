from django.shortcuts import render

from .models import Website
from .forms import WebsiteForm
from django.http import HttpResponseRedirect, Http404


def index(request):
    form = WebsiteForm()

    content = {
      "form"  : form
    }

    if request.method == "GET":
        return render(request, "index.html", content)
    
    if request.method == "POST": 
        form = WebsiteForm(request.POST)

        if form.is_valid():
            formData = form.save()

            longurl = formData.longurl
            newurl = request.build_absolute_uri('/') + formData.shorturl

            print(longurl, newurl)

            content = {
                "longurl": longurl, 
                "newurl" : newurl
            }

            return render(request, "index.html", content)


def redirecturl(request, url):
    try:
        a = Website.objects.get(shorturl = url)
        a.save() 

        return HttpResponseRedirect(a.longurl)
    
    except Exception as e:
        return Http404("The page is lost.")