from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Prashobh'})

def add(request):
    var1 = request.POST['num1']
    var2 = request.POST['num2']
    amount = int(var1) + int(var2)

    return render(request,'result.html',{ 'amount':amount})

    # def add(request):
        # return render(request, 'result.html')
 