from django.http import HttpResponse
from datetime import datetime
from random import randint
from django.shortcuts import render
import subprocess

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