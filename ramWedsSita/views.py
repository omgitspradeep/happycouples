from django.shortcuts import render
from django.http import HttpResponse
from .models import Wisher
from .serializers import WishSerializer
from rest_framework.renderers import JSONRenderer
from django.urls import reverse

# Create your views here.

gallery={
    "Together":{
                "image":"ramWedsSita/images/portfolio/folio01.jpg",
                "desc":"The only exception is that you can call the window.print() method in the browser to print the content of the current window."
                },    
    "Engagement":{
                "image":"ramWedsSita/images/portfolio/folio02.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                },
    "Cool":{
                "image":"ramWedsSita/images/portfolio/folio03.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                },
    "Awesome":{
                "image":"ramWedsSita/images/portfolio/folio04.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                },
    "Lovely":{
                "image":"ramWedsSita/images/portfolio/folio05.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                },
    "Reception":{
                "image":"ramWedsSita/images/portfolio/folio06.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                }
    }

testimonials={
        "dadmom":{
            "bm":{
                "image":"ramWedsSita/images/team/bm.jpg",
                "name":"Dr. Kamala Rijal",
                "desc":"Bride's Mom"
            },
            "bd":{
                "image":"ramWedsSita/images/team/bd.jpg",
                "name":"Er. Bimal Rijal",
                "desc":"Bride's Dad"
            },
            "gm":{
                "image":"ramWedsSita/images/team/gm.jpg",
                "name":"Haridevi Bashyal",
                "desc":"Groom's Mom"
            },
            "gd":{
                "image":"ramWedsSita/images/team/gd.jpg",
                "name":"Dr. Bhaktaraj Bashyal",
                "desc":"Groom's Dad"
            }

        },
        "others":{
            "HajurBuwa/ HajurAma":": First Khanal, Second Khanal",
            "ThuloBuwa/ SanoBuwa":": First/Second, Second/SecondWife, Third/ThirdWife",
            "Didi/Bahini":": First/FirstWife, Second/SecondWife",
            "Daju/Bhai":": First/FirstWife, Second/SecondWife,Third",
            "Bhatija/Bhatiji":": First, Second/SecondWife, Third/ThirdWife, FOurth, Fifth, Sixth, Seventh, Eighth, Ninth, Tenth, Eleventh, Twelveth"
        }
    }

def home(request):
    if request.method == 'POST': 
     name = request.POST.get('Name')
     wish = request.POST.get('Wish')
     try:
         Wisher.objects.create(name=name,wishes=wish)
     except Exception as e:
         print("ERROR IS :  ",e)
         return HttpResponse("Some thing went wrong. Try again ")   
    wishes = Wisher.objects.all()
    return render(request, "ramWedsSita/home.html",context={"wishes":wishes,"testi":testimonials, "gallery":gallery})










