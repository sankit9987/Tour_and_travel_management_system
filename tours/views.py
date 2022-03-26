from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
import razorpay
from tour_and_travels.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            name= request.POST['name']
            email= request.POST['email']
            mobile= request.POST['mobile']
            msg= request.POST['msg']
            Contact.objects.create(name=name,mobile=mobile,email=email,msg=msg)
            return redirect("index")
        p = Place.objects.all()
        return render(request, "home.html",{'p':p})
    else:
        return redirect("user_index")

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)
            if user:
                login(request, user)
                messages.success(request, "login successfully!!!")
                if request.user.is_superuser:
                    return redirect("Dashboard")
                else:
                    return redirect("index")
            else:
                messages.error(request, "Please check username and password!!!")
                return redirect("login")
        return render(request, "login.html")
    else:
        return redirect("index")

def user_logout(request):
    logout(request)
    return redirect("login")

def registration(request):
    if not request.user.is_authenticated:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            name=request.POST['name']
            address=request.POST['address']
            address2=request.POST['address2']
            state=request.POST['state']
            city=request.POST['city']
            zip=request.POST['zip']
            User.objects.create_user(email=email, password=password,name=name,state=state,zip=zip,city=city,Address=address,Address2=address2)
            return redirect("login")
        return render(request, "new-registration.html")
    else:
        return redirect("index")

@login_required(login_url='login')
def user_index(request):
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        mobile= request.POST['mobile']
        msg= request.POST['msg']
        Contact.objects.create(name=name,mobile=mobile,email=email,msg=msg)
        return redirect("user_index")
    p = Place.objects.all()
    return render(request, "user/index.html",{'p':p})

@login_required(login_url='login')
def delete_booking(request,id):
    place = Payment.objects.get(id=id)
    place.delete()
    return redirect("booked")

@login_required(login_url='login')
def booked(request):
    p = Payment.objects.filter(Q(user=request.user) & Q(status="confirm"))
    return render(request, "user/booked.html",{'p':p})


client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
@login_required(login_url='login')
def payment(request,id):
    if request.method=='POST':
        travel_date = request.POST['date']
        name = request.POST['firstname']
        address = request.POST['address']
        place = request.POST['place']
        city = request.POST['city']
        zip = request.POST['zip']
        state = request.POST['state']
        pace = request.POST['place']
        mode = request.POST['mode']
        place = Place.objects.get(id=pace)
        Payment.objects.create(name=name,user=request.user,place=place,travel_date=travel_date,address=address,city=city,zip=zip,state=state,status="confirm")
        if mode=='Cash':
            return redirect("booked")
        else:
            user = Payment.objects.filter(user = request.user)
            user = user[::-1]
            user = user[0]
            amount = place.cost
            pla = place.name
            Booking_amount = int(amount)*100
            orderCurrency = 'INR'
            PaymentOrder = client.order.create(dict(amount=int(Booking_amount),currency=orderCurrency,payment_capture=1))
            paymentID = PaymentOrder['id']
            user.order_id = paymentID
            user.save()
            return render(request, "user/pay.html",{'amount':Booking_amount,'newuser':user,"api_key":RAZORPAY_API_KEY,'order_id':paymentID,"pla":pla})
    p = Place.objects.get(id=id)
    return render(request, "user/payment.html",{'p':p})
    
@login_required(login_url='login')
def place_detail(request,id):
    p = Place.objects.get(id=id)
    return render(request, "user/place details.html",{'p':p})


@login_required(login_url='login')
def add_place(request):
    if request.user.is_superuser:
        if request.method=='POST':
            name = request.POST['name']
            cost = request.POST['cost']
            des = request.POST['des']
            image = request.FILES['image']
            Place.objects.create(name=name,des=des,cost=cost,image=image)
            return redirect("place_list")
        return render(request, "head/add-place.html")
    else:
        return redirect("user_index")

@login_required(login_url='login')
def customer_list(request):
    if request.user.is_superuser:
        p = Payment.objects.all()
        return render(request, "head/customer-list.html",{'p':p})
    else:
        return redirect("user_index")

@login_required(login_url='login')
def place_list(request):
    if request.user.is_superuser:
        place = Place.objects.all()
        return render(request, "head/place-list.html",{'place':place})
    else:
        return redirect("user_index")

@login_required(login_url='login')
def delete_payment(request,id):
    if request.user.is_superuser:
        place = Payment.objects.get(id=id)
        place.delete()
        return redirect("customer_list")
    else:
        return redirect("user_index")

@login_required(login_url='login')
def Dashboard(request):
    if request.user.is_superuser:
        p = Place.objects.all().count()
        u = User.objects.all().count()
        pay = Payment.objects.all().count()
        return render(request, "head/over-view.html",{'p':p,'u':u,'pay':pay})
    else:
        return redirect("user_index")