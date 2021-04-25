from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect


def hblog(request):
    return render(request, "hblogs.html")



def bblog(request):
    return HttpResponse("This page displays the blog on buddhist marriages")



def cblog(request):
    return HttpResponse("This page displays the blog on christian marriages")
