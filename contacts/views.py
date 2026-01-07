from django.shortcuts import render, redirect, get_object_or_404
from .models  import Contact

from django.contrib import messages

from .forms import ContactForm 

# Create your views here.


def contact(request):
    if request.method =='POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email =request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an inquiry for this lisitng')
                return redirect('listings:listing',listing_id=listing_id)
        contact=Contact(listing=listing,listing_id=listing_id, name=name , email=email, phone=phone,message=message, user_id=user_id)
   

        contact.save()
        messages.success(request, 'Your request has benn submitted CLinic representative will get you back soon')


       
def delete_contact(request,contact_id):
    contact = get_object_or_404(Contact, pk=contact_id,klass=Contact)
    print(f"delete contact: {contact}")
    contact.delete()
    return redirect('accounts:dashboard')

def edit_contact(request,contact_id):
    #Logic to edit the contact with given contact_ID
  
    if request.method == "POST":
        form=ContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save
            return redirect('accounts:dashboard')
    else:
        form = ContactForm(instance=contact)

    return render(request,"contacts/edit_contact.html",{"form":form,"contact":contact})
