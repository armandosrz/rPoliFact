from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'final/index.html')

def data(request):
    return render(request, 'final/data.html')

def model(request):
    return render(request, 'final/model.html')

def topic(request):
    return render(request, 'final/topic.html')

def g_all(request):
    return render(request, 'final/graph_all.html')

def g_bias(request):
    return render(request, 'final/graph_bias.html')

def g_confirmed(request):
    return render(request, 'final/graph_confirmed.html')

def g_false(request):
    return render(request, 'final/graph_false.html')

def g_mostlyFalse(request):
    return render(request, 'final/graph_mostly_false.html')

def g_mostlyTrue(request):
    return render(request, 'final/graph_mostly_true.html')

def g_none(request):
    return render(request, 'final/graph_none.html')

def g_verify(request):
    return render(request, 'final/graph_verify.html')
