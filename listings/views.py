from django.shortcuts import render

def index(request):
    return render(request,'listings/listings.html')

def listing(request):
    return render(request,'listings/listing.html')
