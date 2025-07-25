from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import WisherRS,InviteeRS
from rest_framework.renderers import JSONRenderer
from django.urls import reverse
from pyshorteners import Shortener
from rest_framework.decorators import api_view

# Create your views here.

gallery={
    "Lovely":{
                "image":"ramWedsSita/images/gallery/gallery01.jpg",
                "desc":"The only exception is that you can call the window.print() method in the browser to print the content of the current window."
                },    
    "Awesome":{
                "image":"ramWedsSita/images/gallery/gallery02.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                },
    "Cool":{
                "image":"ramWedsSita/images/gallery/gallery03.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                },
    "Engagement":{
                "image":"ramWedsSita/images/gallery/gallery04.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                },
    "Together":{
                "image":"ramWedsSita/images/gallery/gallery05.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                },
    "Celebration":{
                "image":"ramWedsSita/images/gallery/gallery06.jpg",
                "desc":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore architecto nobis voluptatum enim mollitia odit totam laudantium, quo reprehenderit nihil quis praesentium nam nulla veniam rerum in itaque quos dolor."
                }
    }

testimonials={
        "dadmom":{
            "bm":{
                "image":"ramWedsSita/images/team/bm.png",
                "name":"Dr. Kamala Rijal",
                "desc":"Bride's Mom"
            },
            "bd":{
                "image":"ramWedsSita/images/team/bd.png",
                "name":"Er. Bimal Rijal",
                "desc":"Bride's Dad"
            },
            "gm":{
                "image":"ramWedsSita/images/team/gm.png",
                "name":"Haridevi Bashyal",
                "desc":"Groom's Mom"
            },
            "gd":{
                "image":"ramWedsSita/images/team/gd.png",
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



def index(request, inviteeCode):
    try:
        invitedGuest=InviteeRS.objects.get(secretCode=inviteeCode)
        print(f"Your id is :{inviteeCode} and {invitedGuest.name}")
        # Update the value to set the user has visited site.
        if not invitedGuest.siteVisited:
            invitedGuest.siteVisited=True
            invitedGuest.save()
        
        # We store seesion everytime. User visits landing page because they can request landing page from same browser appending different inviteeCode in url
        request.session['guestsession']=inviteeCode
        print(f"Your session is :{inviteeCode}")

    except Exception as e:
        # No user with requested inviteeCode
        print(e)
        return HttpResponse("No page found Index")

    wishes = WisherRS.objects.all()
    if len(wishes) == 0:
        return render(request, "ramWedsSita/home.html",context={"alreadyWished":0,"testi":testimonials, "gallery":gallery, "inviteeObj":invitedGuest})

    # Has this invitee already wished? if so, don't show wish form in landing page.
    return render(request, "ramWedsSita/home.html",context={"wishes": wishes,"alreadyWished":alreadyWished(inviteeCode,wishes),"testi":testimonials, "gallery":gallery,"inviteeObj":invitedGuest})



def alreadyWished(inviteeCode, wisherObjs):
    flag=0
    for wisherObj in wisherObjs:
        if (inviteeCode==wisherObj.invitee.secretCode):
           flag=1
           break
    return flag



def getSessionID(request):
    return request.session['guestsession']



    #Implement AJAX in frontend and remove redirection to index
def home(request):
    if request.method == "POST":
        print("-------------HOME POST------------")
        inviteeCode = getSessionID(request)
        wish = request.POST.get('Wish')
        invitedGuest=InviteeRS.objects.get(secretCode=inviteeCode)
        print(f" ID: {inviteeCode} and WISH: {wish}")
        WisherRS.objects.create(invitee=invitedGuest,wishes=wish)
        return HttpResponseRedirect(reverse('index',args=(inviteeCode,) ))

    elif request.method == "GET":
        print("-------------HOME GET------------")
        inviteeCode=getSessionID(request)
        try:
            inviteeObj=InviteeRS.objects.get(secretCode=inviteeCode)
            WisherRS.objects.get(invitee=inviteeObj).delete()
            return JsonResponse({"status":"1","msg":"Successful"})  
        except Exception as e:
            return JsonResponse({"status":"0","msg":"Unsuccessful"})
    else:
        return HttpResponse("No page found GET")
        
@api_view(['GET'])
def getAllGuestData(request):
    items=[]
    guests = InviteeRS.objects.all()

    for g in guests:
        guestWish = g.getWishIfExists()
        items.append({'name': g.name,'visited':g.siteVisited,'address':g.address, 'url':g.URL(),'message':g.inviteeMessage,'status':g.inviteStatus,'wish':guestWish})
    
    print(items)
    return JsonResponse(items,safe=False)


def shortenURL(longUrl):
    return Shortener().clckru.short(longUrl)