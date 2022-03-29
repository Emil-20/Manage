from django.shortcuts import render, redirect
from mapp.models import Contact, Enquiry
from django.contrib.auth.models import auth, User


# Create your views here.


def home(request):
    return render(request, 'main.html')


def enquiry(request):
    return render(request, 'enquiry.html')


def contact(request):
    return render(request, 'contact.html')


def software(request):
    return render(request, 'software.html')


def training(request):
    return render(request, 'training.html')


def autodealers(request):
    return render(request, 'auto-dealers.html')


def bank(request):
    return render(request, 'bank.html')


def consultancies(request):
    return render(request, 'consultancy.html')


def employement(request):
    return render(request, 'employment.html')


def malls(request):
    return render(request, 'malls.html')


def motor_showroom(request):
    return render(request, 'motor-showroom.html')


def rentals(request):
    return render(request, 'Rentals.html')


def service_stations(request):
    return render(request, 'service.html')


def grocery(request):
    return render(request, 'grocery.html')


def supermarkets(request):
    return render(request, 'supermarket.html')


def restaurant(request):
    return render(request, 'restaurant.html')


def financialinstitution(request):
    return render(request, 'finance.html')


def telecommunication(request):
    return render(request, 'telecommunication.html')


def architecture(request):
    return render(request, 'architecture.html')


def catering(request):
    return render(request, 'cater.html')


def construction(request):
    return render(request, 'construction.html')


def educational(request):
    return render(request, 'education.html')


def electrical(request):
    return render(request, 'electrical.html')


def entertainment(request):
    return render(request, 'entertainment.html')


def event(request):
    return render(request, 'event.html')


def hospital(request):
    return render(request, 'hospital.html')


def jewel(request):
    return render(request, 'jewel.html')


def manufacturing(request):
    return render(request, 'manufacture.html')


def marketing(request):
    return render(request, 'market.html')


def realestate(request):
    return render(request, 'real-estate.html')


def storage(request):
    return render(request, 'storage.html')


def transportation(request):
    return render(request, 'transport.html')


def travel(request):
    return render(request, 'travel.html')


def esearch(request):
    member1 = Enquiry.objects.all()
    if 'esearch' in request.POST:
        searchi = request.POST['esearch']
        srch1 = Enquiry.objects.filter(id=searchi)
        return render(request, 'edash.html', {'srch1': srch1, 'member1': member1})


def msearch(request):
    member = Contact.objects.all()
    if 'msearch' in request.POST:
        searchi = request.POST['msearch']
        srch = Contact.objects.filter(id=searchi)
        return render(request, 'mdash.html', {'srch1': srch, 'member': member})

    else:
        srch = Contact.objects.all()
        return render(request, 'contact.html', {'srch1': srch})


def Addcon(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        print(email)
        phone = request.POST.get('ccode')
        print(phone)
        message = request.POST.get('message')
        print(message)
        data = Contact(Name=name, Email=email, Phone=phone, Messages=message)
        data.save()
        return render(request, 'main.html')
    else:
        return render(request, 'contact.html')


def Addenq(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        designation = request.POST.get('designation')
        print(designation)
        country = request.POST.get('country')
        print(country)
        state = request.POST.get('state')
        print(state)
        city = request.POST.get('city')
        print(city)
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        phone = request.POST.get('ccode')
        message = request.POST.get('message')
        data = Enquiry(Name=name, Designation=designation, Country=country, State=state,
                       City=city, Pin=pin, Email=email, Phone=phone, Messages=message)
        data.save()
        return render(request, 'main.html')
    else:
        return render(request, 'enquiry.html')


def admin(request):
    return render(request, 'admin.html')


def registration(request):
    return render(request, 'registration.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        if cpassword == password:
            try:
                user1 = User.objects.create_user(first_name=fname, last_name=lname, username=username,
                                                 password=password, email=email)
                user1.save()
                return render(request, 'admin.html')
            except:
                return render(request, 'registration.html')
        else:
            return render(request, 'registration.html')


def login(request):
    member = Contact.objects.all()
    count = Enquiry.objects.all()
    count1 = Enquiry.objects.all().count()
    member1 = Contact.objects.all().count()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = auth.authenticate(username=username, password=password)
        if u is not None:
            auth.login(request, u)
            return render(request, 'dash.html', {'member': member, 'count1': count1, 'member1': member1, 'count': count})
        else:

            return render(request, 'admin.html')
    else:
        return render(request, 'admin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def dash(request):
    member1 = Contact.objects.all().count()
    count1 = Enquiry.objects.all().count()
    return render(request, 'dash.html', {'member1': member1, 'count1':count1})


def mdash(request):
    member = Contact.objects.all()
    return render(request, 'mdash.html', {'member': member})


def edash(request):
    member1 = Enquiry.objects.all()
    return render(request, 'edash.html',{'member1': member1})


def erp(request):
    return render(request, 'erp.html')


def accounting(request):
    return render(request, 'accounting.html')


def treasury(request):
    return render(request, 'treasury.html')


def receivable(request):
    return render(request, 'receivable.html')


def supply(request):
    return render(request, 'supply.html')


def asset(request):
    return render(request, 'asset.html')


def plc(request):
    return render(request, 'plc.html')


def customer(request):
    return render(request, 'customer.html')


def shop(request):
    return render(request, 'shop.html')


def commerce(request):
    return render(request, 'commerce.html')


def sales(request):
    return render(request, 'sales.html')


def serve(request):
    return render(request, 'serve.html')


def exp1(request):
    return render(request, 'exp1.html')


def core(request):
    return render(request, 'core.html')


def talent(request):
    return render(request, 'talent.html')


def workforce(request):
    return render(request, 'workforce.html')


def finbank(request):
    return render(request, 'finbank.html')


def insurance(request):
    return render(request, 'insurance.html')


def agri(request):
    return render(request, 'agri.html')


def cpro(request):
    return render(request, 'cpro.html')


def fashion(request):
    return render(request, 'fashion.html')


def life(request):
    return render(request, 'life.html')


def retail(request):
    return render(request, 'retail.html')


def wholesale(request):
    return render(request, 'wholesale.html')


def media(request):
    return render(request, 'media.html')


def engineering (request):
    return render(request, 'engineering.html')


def sports (request):
    return render(request, 'sports.html')


def tele2 (request):
    return render(request, 'tele2.html')

