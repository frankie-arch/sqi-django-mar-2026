from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def books(request):
    return HttpResponse("""<ul><li>Othello</li></li> 
                        <li>Time Machine</li> 
                        <li>Romeo and Julliet</li> 
                        <li>The midsummer night dream</li> 
                        <li>The life changer</li></ul>""")

def special(request):
    return HttpResponse("""<div><li>Othello</li>
                        <li>The midsummer night dream</li></div>""")
