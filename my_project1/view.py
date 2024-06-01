from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    #word = render(request,"django.html")
    word= 10+1 



    return render(request,"django.html")

def hey_man(requset):
   return render(requset ,"daum.html")