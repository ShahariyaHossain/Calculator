from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# this funciton will render the normal calculator page
def normal_cal(request):
    return HttpResponse("<h1>Hellor world</h1><hr><p>This is the <b>normal calculator page</b>.</p>")