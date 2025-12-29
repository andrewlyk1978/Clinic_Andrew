from django.shortcuts import render

#from django.http import HttpResponse

from listings.models import Listing
# Create your views here. (ERB8 )
# Let listings-> apps , call data class 

def index (request):
    listings = Listing.objects.all()
        # Cisco command 
    context = {"listings": listings}
    return render(request, 'pages/index.html', context)
    # For multitables for mulit databse 
    
    
    # return HttpResponse("<h1>hello</h1>")
    #print(request,'pages/index.html')
    #return render(request, 'pages/index.html')


def about (request):
    print(request,'pages/about.html')
    return render(request,'pages/about.html')

