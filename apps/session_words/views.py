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
        if 'all_words' not in request.session:
            request.session['all_words']=[]
        else:
            request.session['all_words']=request.session['all_words']
        context={
        'addword':request.POST['addword'],
        'color':request.POST['color'],
        'big':request.POST['big'],
        'time':datetime.now().strftime(" - added on %H:%M %p, %B %d, %Y")
        }
        request.session['all_words'].append(context)
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    print "testing here"
    del request.session['addword']
    return redirect('/')
