from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def date_time(request):
    date=datetime.datetime.now()
    s='<body> bgcolor="seashell"</body>'
    s='<h1>Current date & time is:='+str(date)+'</h1>'
    return HttpResponse(s)
