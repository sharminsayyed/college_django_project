"""
URL configuration for BlueNile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    # superuser
    path('admin/', admin.site.urls),
    # frontend 
    path('',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('menu/',views.menu,name='menu'),
    path('events/',views.events,name='events'),
    path('gallery/',views.gallery,name='gallery'),
    path('chefs/',views.chefs,name='chefs'),
    path('booktable/',views.booktable,name='booktable'),
    path('contact/',views.contact,name='contact'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    # dashboard admin page
    path('dashboard/',views.dashboard,name='dashboard'),
    # logout redirect to home page 
    path('logout/',views.adminlogout,name='adminlogout'),
    # fetching all the tables 
    path('enquiryinfo/',views.enquiryinfo,name='enquiryinfo'),
    path('bookinginfo/',views.bookinginfo,name='bookinginfo'),
    path('eventinfo/',views.eventinfo,name='eventinfo'),
    #  deleting records from all the table
    path('delete_enquiry_record/<int:id>/',views.delete_enquiry_record,name='delete_enquiry_record'),
    path('delete_booking_record/<int:id>/',views.delete_booking_record,name='delete_booking_record'),
    path('delete_event_record/<int:id>/',views.delete_event_record,name='delete_event_record'),
    #  edit and update the records from the table 
    path('edit_enquiry_record/<int:id>/',views.edit_enquiry_record,name='edit_enquiry_record'),
    path('update_enquiry_record/<int:id>',views.update_enquiry_record,name='update_enquiry_record'),
    path('edit_booking_record/<int:id>/',views.edit_booking_record,name='edit_booking_record'),
    path('update_booking_record/<int:id>',views.update_booking_record,name='update_booking_record'),
    path('edit_event_record/<int:id>/',views.edit_event_record,name='edit_event_record'),
    path('update_event_record/<int:id>',views.update_event_record,name='update_event_record'),
    # api data for the tables 
    path('enquiry_api/',views.enquiry_data.as_view(),name='enquiry_data'),
    path('booking_api/',views.booking_data.as_view(),name='table_booking_data'),
    path('event_api/',views.event_data.as_view(),name='table_event_data'),



]
