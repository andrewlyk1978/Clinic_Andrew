from django.shortcuts import render

#from django.http import HttpResponse

from listings.models import Listing


from doctors.models import Doctor

from listings.choices import district_choices, room_choices, rooms_choices

#TODO : update index and about views
# @ dafrag
# ? list latest listin 


# Create your views here. (ERB8 )
# Let listings-> apps , call data class 

def index (request):
    listings = Listing.objects.all()
    #listings= Listing.object.order_by('-list_date').filter(is_published=True)[:3]
        # Cisco command filter() excliude order()
    context = {"listings": listings,
               "district_choices":district_choices,
               "room_choices": room_choices,
               "rooms_choices": room_choices
               }
    
    return render(request, 'pages/index.html', context)
    # For multitables for mulit databse 
    
    
    # return HttpResponse("<h1>hello</h1>")
    #print(request,'pages/index.html')
    #return render(request, 'pages/index.html')


def about (request):
    doctors=Doctor.objects.order_by("-hire_date")[:3]
    mvp_doctors =Doctor.objects.all().filter(is_mvp=True)
    #print(request,request.path)
    context={"doctors":doctors,"mvp_doctors":mvp_doctors}
    return render(request,'pages/about.html',context)

