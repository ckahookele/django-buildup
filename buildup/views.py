from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from random import randint
from django.shortcuts import render
from buildup.models import Fact
from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import subprocess

class FactForm(forms.Form):
        text = forms.CharField(label="Fact", max_length=255)

def hello(request):
    return HttpResponse("Hello there!")
def time(request):
    return HttpResponse("The time is " + str(datetime.now()))
def random(request):
    return HttpResponse(str(randint(1,10)))
def hello_name(request, yourname):
    return HttpResponse(str("Hello " + yourname))
def sentence(request,sentence):
    return HttpResponse(subprocess.call(["say", sentence]))

def hello_template(request, yourname):
    return render(request, "hello.html", { "yourname": yourname, "foobar":12 })
def time_template(request):
    return render(request, "time.html", { "time": str(datetime.now())})
def random_template(request):
    return render(request, "random.html", {"random": str(randint(1,10))})
def speak_template(request, sentence):
    return render(request, "speak.html", {"sentence": subprocess.call(["say", sentence])})

def all_facts(request):
    return render(request, "all_facts.html", { "facts": Fact.objects.all() })

@login_required
def new_fact(request):
    # someone wants to create a fact
    if request.method == "GET":
        form = FactForm()
        return render(request, "new_fact.html", { "form": form })
    else:
        # someone submitted the form so we need to save the data
        form = FactForm(request.POST)
    if form.is_valid():
        # TODO actually actually save the new fact
        fact = Fact(text =form.cleaned_data['text'], author = request.user, created_date = datetime.now())
        fact.save()
        # and redirect to the all_facts page
        return HttpResponseRedirect(reverse('all_facts'))
    else:
        # return the form and display the errors
        return render(request, "new_fact.html", { "form": form })
        return HttpResponse(form.cleaned_data['text'], form.cleaned_data['author'])