from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests, sys
from subprocess import run,PIPE

#def hello(request):
#  return HttpResponse("Hello this is our first program")
    
def external(request):
    try:
        inp=request.POST.get('params')
    except:
        raise("Sorry wrong entities")

    out=run([sys.executable,'C:\\Users\\Santhosh\\Desktop\\actual.py',inp], shell=False , stdout=PIPE)
    print(out)

    return render(request, 'base.html', {'data':out.stdout})