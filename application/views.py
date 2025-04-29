from django.shortcuts import render ,redirect
# import model file where all tables are created
from application.models import*
# to display message after submission
from django.contrib import messages
# for authentication login logout 
from django.contrib.auth import authenticate, login , logout 
# python decorator to restrict the login 
from django.contrib.auth.decorators import login_required
# for api 
from rest_framework.response import Response
from rest_framework.views import APIView
from application.serializers import *

# Create your views here.

def home(request):
    return render (request,'index.html')

def services(request):
    return render(request,'services.html')

def menu(request):
    return render(request,'menu.html')

def events(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('date')
        e = request.POST.get('time')
        f = request.POST.get('people')
        g = request.POST.get('eventname')
        h = request.POST.get('message')

        info = event_table(name =a ,email=b,phone=c,date =d,time=e,people=f,eventname =g,message=h,)

        info.save()

        messages.success(request,'Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!')

    return render(request,'events.html')

def gallery(request):
    return render(request,'gallery.html')

def chefs(request):
    return render(request,'chefs.html')

def booktable(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('date')
        e = request.POST.get('time')
        f = request.POST.get('people')
        g = request.POST.get('message')

        info = book_table(name =a ,email=b,phone=c,date =d,time=e,people=f,message=g,)

        info.save()

        messages.success(request,'Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!')

    return render(request,'book.html')

    

def contact(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('enquiry')
        e = request.POST.get('message')

        info = contact_table(name =a ,email=b,phone=c,enquiry=d,message=e)

        info.save()

        messages.success(request,'Your message has been sent. Thank you!')

    return render(request,'contact.html')



# dashboard 
def adminlogin(request):
    if request.method=="POST":
        a = request.POST.get('username')
        b = request.POST.get('password')

        #if the username and password is valid then user object is return if it is invalid then None is returned 
        user =authenticate(request, username=a , password =b)

        if user is not None :
            # logged in using the default login function 
            login(request,user)
            #redirect to another page use the technical name
            return redirect('dashboard')
        else:
            messages.error(request,'Incorrect Username and Password (only owner/staff should login)')

    return render(request,'login.html')

def adminlogout(request):
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    return render (request,'dashboard/index.html')

@login_required
def enquiryinfo(request):
    data = contact_table.objects.all().order_by('-id')
    dict={'information':data}
    return render (request,'dashboard/enquiry.html',dict)

@login_required
def bookinginfo(request):
    data = book_table.objects.all().order_by('-id')
    return render (request,'dashboard/booking.html',{'information':data})

@login_required
def eventinfo(request):
    data = event_table.objects.all().order_by('-id')
    return render (request,'dashboard/events_info.html',{'information':data})


def delete_enquiry_record(request ,id):
    data = contact_table.objects.get(pk=id)
    data.delete()
    return redirect('enquiryinfo')


def delete_booking_record(request,id):
    data = book_table.objects.get(pk=id)
    data.delete()
    return redirect('bookinginfo')

def delete_event_record(request,id):
    data = event_table.objects.get(pk=id)
    data.delete()
    return redirect('eventinfo')


def edit_enquiry_record(request,id):
    info = contact_table.objects.filter(pk=id)
    data ={'information':info}
    return render(request,'dashboard/edit_enquiry.html',data)


def update_enquiry_record(request, id):
    info = contact_table.objects.get(pk =id)
    info.contacted = request.POST.get('contacted')
    info.save()
    return redirect('enquiryinfo')


def edit_booking_record(request, id):
    info = book_table.objects.filter(pk=id)
    data ={'information':info}
    return render(request,'dashboard/edit_booking.html',data)


def update_booking_record(request,id):
    info = book_table.objects.get(pk=id)
    info.date = request.POST.get('date')
    info.time =request.POST.get('time')
    info.people=request.POST.get('people')
    info.contacted=request.POST.get('contacted')
    info.reservation=request.POST.get('reservation')
    info.save()
    return redirect('bookinginfo')


def edit_event_record(request,id):
    info=event_table.objects.filter(pk=id)
    data = {'information':info}
    return render(request,'dashboard/edit_event.html',data)

def update_event_record(request,id):
    info = event_table.objects.get(pk=id)
    info.date = request.POST.get('date')
    info.time =request.POST.get('time')
    info.people=request.POST.get('people')
    info.contacted=request.POST.get('contacted')
    info.reservation=request.POST.get('reservation')
    info.save()
    return redirect('eventinfo')


#  api data fetching 

class enquiry_data(APIView):
    def get(self,request,format=None):
        data = contact_table.objects.all()
        serializer = contact_tableSerializers(data,many=True)
        return Response(serializer.data)
    
class booking_data(APIView):
    def get(self,request,format=None):
        data = book_table.objects.all()
        serializer = book_tableSerializers(data,many=True)
        return Response(serializer.data)
class event_data(APIView):
    def get(self,request,format=None):
        data = event_table.objects.all()
        serializer = event_Serializers(data,many=True)
        return Response(serializer.data)
 