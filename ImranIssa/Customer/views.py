from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render,redirect
from Customer.models import Packages,Customer
from django.db import connection,IntegrityError
from django.contrib import messages
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import psycopg2
# Create your views here.
cursor = connection.cursor()

additional_charges = 50000


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def home(request):

    return render(request,'Customer/home.html',)



def packages(request):
   
    package_1 = Packages.objects.get(package_id=1)  # select * from packages where package_id=1
    package_2 = Packages.objects.get(package_id=2)  # select * from packages where packages_id=2
    package_3 = Packages.objects.get(package_id=3)  # select * from packages where packages_id=3

    #Calculating Package Price 

    #Package 1
    total_days_makkah = int(package_1.makkah_days_1 + package_1.makkah_days_2) 
    makkah_hotel_charges = total_days_makkah * int(package_1.hotel.per_night)
    madina_hotel_charges = int(package_1.hotel_madina.per_night) * package_1.madina_days
    total_hotel_charges_1 = makkah_hotel_charges + madina_hotel_charges

    #Package 2
    total_days_makkah = int(package_2.makkah_days_1 + package_2.makkah_days_2)
    makkah_hotel_charges = total_days_makkah * int(package_2.hotel.per_night)
    madina_hotel_charges = int(package_2.hotel_madina.per_night) * package_2.madina_days
    total_hotel_charges_2 = makkah_hotel_charges + madina_hotel_charges

    #Package 3
    total_days_makkah = int(package_3.makkah_days_1 + package_3.makkah_days_2)
    makkah_hotel_charges = total_days_makkah * int(package_3.hotel.per_night)
    madina_hotel_charges = int(package_3.hotel_madina.per_night) * package_3.madina_days
    total_hotel_charges_3 = makkah_hotel_charges + madina_hotel_charges
   
    price_1 = int(package_1.food) + total_hotel_charges_1 + additional_charges
    price_2 = int(package_2.food) + total_hotel_charges_2 + additional_charges
    price_3 = int(package_3.food) + total_hotel_charges_3 + additional_charges
    
    return render(request,'Customer/packages.html',{'package_1':package_1,'package_2':package_2,"package_3":package_3,'price_1':price_1,'price_2':price_2,'price_3':price_3})

def package_detail(request,pk):
   
    #cursor.execute("select * from packages where package_id=(%s)",(pk))
    
    #Same as above but iterating over the above query is much more diffcult as it returns a dictionary of lists
    package = Packages.objects.get(package_id=pk)
    return render(request,'Customer/package_detail.html',{'i':package})

def customer_detail_pk(request,pk):
    
    if request.method =='POST':
        
        name = request.POST['name']
        passport = request.POST['passport']
        address = request.POST['address']
        dp_date = str(request.POST['depart'])
        ar_date = str(request.POST['arrival'])
        dp_p = request.POST['dp_p']       #depart from pakistan
        ar_s = request.POST['ar_s']        #arrival in saudi arabia
        dp_s = request.POST['dp_s']        #depart from saudi arabia
        ar_p = request.POST['ar_p']        # arrival in Pakistan
        package = request.POST['package']
        try:
            cursor.execute('Insert into customer(name,pass_id,address,depart_date,arrival_date,depart_origin,arrival_origin,depart_origin_1,arrival_origin_1,package_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            ,(name,passport,address,dp_date,ar_date,dp_p,ar_s,dp_s,ar_p,package))
            return redirect('register')
        except IntegrityError:
            HttpResponseNotAllowed('<p>The Passport no provided already registered')
            messages.info(request,'Passport Already Registered')    
    
    
    cursor.execute("select * from packages where package_id=(%s)",(pk))

    package = Packages.objects.get(package_id=pk)
 
    flag = True

    return render(request,'Customer/customer_detail.html',{'package':package,'flag':flag})


def customer_detail(request):
    flag = False

    if request.method =='POST':
        cursor = connection.cursor()
        name = request.POST['name']
        passport = request.POST['passport']
        address = request.POST['address']
        dp_date = str(request.POST['depart'])
        ar_date = str(request.POST['arrival'])
        dp_p = request.POST['dp_p']       #depart from pakistan
        ar_s = request.POST['ar_s']        #arrival in saudi arabia
        dp_s = request.POST['dp_s']        #depart from saudi arabia
        ar_p = request.POST['ar_p']        # arrival in Pakistan
        package = request.POST['package']
        try:
            cursor.execute('Insert into customer(name,pass_id,address,depart_date,arrival_date,depart_origin,arrival_origin,depart_origin_1,arrival_origin_1,package_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            ,(name,passport,address,dp_date,ar_date,dp_p,ar_s,dp_s,ar_p,package))
            return redirect('register')
        except InterfaceError as exc:
            cursor = connection.cursor()
            return redirect('customer_detail')
        except IntegrityError:
            HttpResponseNotAllowed('<p>The Passport no provided already registered')
            messages.info(request,'Passport Already Registered')
            #raise Http404
    

    return render(request,'Customer/customer_detail.html',{'flag':flag})


def register(request):
    return render(request,'Customer/register.html')

def detail(request):
    available = False
    entered = False
    if request.method == "POST":
        passport_no = request.POST['passport']
        #cursor.execute("select * from customer where pass_id=(%s)",(passport_no))
        #x = dictfetchall(cursor)
        try:
            customer = Customer.objects.get(pass_id=passport_no)
            print(type(customer))
            available = True
            entered = True
            return render(request,'Customer/details.html',{'customer':customer,'available':available,'entered':entered})
        except ObjectDoesNotExist:
            not_available = True
            return render(request,'Customer/details.html',{'not_available':not_available})
    return render(request,'Customer/details.html',{'entered':entered,'available':available})
