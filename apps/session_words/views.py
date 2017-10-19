from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    # try:
    #     request.session['addword']
    # except KeyError:
    #     request.session['addword']=[]
    return render(request, 'session_words/index.html')

def process(request):
    if request.method == "POST":
        request.session['addword']=request.POST['addword']
        request.session['color']=request.POST['color']
        request.session['big']=request.POST['big']
        request.session['time']=datetime.now().strftime(" - added on %H:%M %p, %B %d, %Y")
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    print "testing here"
    del request.session['addword']
    return redirect('/')
