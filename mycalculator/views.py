from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# This function will render the home page
def home(request):
    return render(request, 'index.html')

# this funciton will render the calculator page
def normal_cal(request):
    return HttpResponse("<h1>Hellor world</h1><hr><p>This is the <b>normal calculator page</b>.</p><hr><p> Addition: <b>2 + 2 = 4</b></p><p> Subtraction: <b>5 - 3 = 2</b></p><p> Multiplication: <b>3 * 4 = 12</b></p><p> Division: <b>8 / 2 = 4</b></p><br><a href='/'>Go to Home</a>")