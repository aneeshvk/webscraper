from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.form import UregCreate
from app.websraper import webSraping
from .models import ureg, ngoreg
from hashlib import sha256
from .models import creg
from .models import upload
from .models import newproject
from .models import expenditure
from django.contrib import messages
import random


# Create your views here.
def function(request):
    return render(request, 'index.html')


def allngo(request):
    works = ngoreg.objects.all()
    return render(request, 'allngos.html', {'ngos': works})


def allcreg(request):
    works = creg.objects.all()
    return render(request, 'allcouncillor.html', {'creg': works})


def allureg(request):
    works = ureg.objects.all()
    return render(request, 'allureg.html', {'creg': works})


def do_sraping(request):
    #works = ureg.objects.all()
    if request.method == 'POST':
        website_url= request.POST.get('urltoget')
        e1= request.POST.get('outer')
        a1= request.POST.get('attribute1')
        v1= request.POST.get('value1')
        e2= request.POST.get('innerelement')
        a2= request.POST.get('attribute2')
        v2= request.POST.get('value2')
        dataget=webSraping(website_url, e1, a1, v1, e2, a2, v2)
        return render(request, 'result.html',{'result':dataget})
    return render(request, 'doScarping.html')


def changestatus_customer(request, customer_id):
    customer_id = int(customer_id)
    try:
        customer_shelf = ureg.objects.get(id=customer_id)
    except ureg.DoesNotExist:
        return redirect('allureg')
    customer_shelf.status = not customer_shelf.status
    customer_shelf.save(update_fields=['status'])
    # HttpResponse("Something went wrong click <a href= "">{{x}}Reload</a>")
    # if customer_form.is_valid():
    #     customer_form.save()
    #     messages.success(request, 'User profile updated')
    #     if request.session['member_type'] == 'customer':
    #         return render(request, 'companyhome.html')
    return redirect('allureg')
    # return render(request, 'newcustomer.html', {'upload_form': customer_form, 'formname': ' Edit User'})


def update_ureg(request):
    customer_id = int(request.session['member_id'])
    try:
        customer_shelf = ureg.objects.get(id=customer_id)
    except ureg.DoesNotExist:
        return redirect('customer_all')
    customer_form = UregCreate(request.POST or None, instance=customer_shelf)
    if customer_form.is_valid():
        password = customer_form.cleaned_data['password']
        password2 = sha256(password.encode()).hexdigest()
        customer_shelf.password = password2
        try:
            customer_shelf.save(update_fields=['firstname', 'lastname', 'email', 'password'])
            messages.success(request, 'User profile updated')
            if request.session['member_type'] == 'euser':
                return render(request, 'home.html')
            return redirect('allureg')
        except:
            messages.error(request, 'User profile Not updated')
            return render(request, 'home.html')
    return render(request, 'newcustomer.html', {'upload_form': customer_form, 'formname': ' Edit Profile'})

def delete_ureg(request, customer_id):
    customer_id = int(customer_id)
    try:
        customer_shelf = ureg.objects.get(id=customer_id)
    except ureg.DoesNotExist:
        return redirect('allureg')
    customer_shelf.delete()
    return redirect('allureg')



def ngo_delete(request, id):
    ngo_id = int(id)
    try:
        student_shelf = ngoreg.objects.get(id=ngo_id)
    except ngoreg.DoesNotExist:
        return redirect('useruallngo')
    student_shelf.delete()
    return redirect('useruallngo')


def register(request):
    return render(request, 'register.html')


def capp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        clogin(username=username, password=password).save()

    return render(request, 'councilor1login.html')


def glogin(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('pass1')
        if email == 'admin' and password == 'admin':
            request.session['member_id'] = 0
            request.session['member_type'] = "admin"
            request.session['name'] = 'admin'
            return redirect('home')
        else:
            return render(request, 'glogin.html', {'msg': 'Invalid Login Values'})

    return render(request, 'glogin.html', {'msg': ''})


def ngologin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = sha256(password.encode()).hexdigest()
        user = ngoreg.objects.filter(email=email, password=password2)
        if user:
            user_details = ngoreg.objects.get(email=email, password=password2)
            id = user_details.id
            username_user = user_details.email
            request.session['member_id'] = id
            request.session['member_type'] = "ngo"
            request.session['name'] = user_details.name
            return redirect('home')
        else:
            return render(request, 'ngologin.html', {'msg': 'Invalid Login Values'})

    return render(request, 'ngologin.html', {'msg': ''})


def usignin(request):
    return render(request, 'usignin.html')


def csignin(request):
    return render(request, 'csignin.html')


def userviews(request):
    return render(request, 'userview.html')


def cviews(request):
    return render(request, 'councilorview.html')


# def gviews(request):
#      if request.method=='POST':
#           projectdetails=request.POST.get('projectdetails')
#           place=request.POST.get('place')
#           funddetails=request.POST.get('funddetails')
#           newproject(projectdetails=projectdetails, place= place,funddetails=funddetails).save()
#      return render(request,'gvtview.html') 
def uregister(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        place = request.POST.get('place')
        gender = request.POST.get('gender')
        mp = request.POST.get('mp')
        ward = request.POST.get('ward')
        if not validatepssword(pass1):
            messages.error(request, 'Invalid Password')
            return render(request, 'userregistration.html')
        password = sha256(pass1.encode()).hexdigest()
        try:
            ureg(firstname=firstname, lastname=lastname, email=email, password=password, place=place, gender=gender,
                 mp=mp,
                 ward=ward).save()
            messages.success(request, 'User Registration completed!!')
        except:
            messages.error(request, 'Username already existing!!')

    return render(request, 'userregistration.html')


def app(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = sha256(password.encode()).hexdigest()
        user = ureg.objects.filter(email=email, password=password2)
        if user:
            user_details = ureg.objects.get(email=email, password=password2)
            id = user_details.id
            if not user_details.status:
                msg="You are blocked by admin..."
                #messages.error(request, 'You are blocked by admin...')
                return render(request, 'userlogin1.html',{'msg':msg})
            username_user = user_details.email
            request.session['member_id'] = id
            # request.session['member_type'] = "euser"
            request.session['name'] = user_details.firstname
            request.session['member_type'] = ''
            otp = random.randint(1111, 9999)

            f = open("otp.txt", "w")
            f.write("Your OTP Is " + str(otp))
            f.close()
            request.session['otp'] = otp
            # u_email = m.email
            # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            #     smtp.ehlo()
            #     smtp.starttls()
            #     smtp.ehlo()
            #     smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PWD)
            #     subject = 'Login Using'
            #     body = 'Your OTP : ' + otp
            #     msg = f'Subject:{subject}\n\n{body}'
            #     smtp.sendmail(settings.EMAIL_ADDRESS, u_email, msg)
            return render(request, 'login2.html', {'otp': otp})

            # return redirect('home')

    return render(request, 'userlogin1.html')


def login_level2_student(request):
    if request.method == 'POST':
        x = int(request.POST['otp'])
        y = int(request.session['otp'])
        if x == y:
            del request.session['otp']
            request.session['member_type'] = 'euser'
            return redirect('home')
        else:
            return HttpResponse(
                "<div style='margin-left:15%;margin-top:15%' >Your username and password didn't match.<a href='' %}'>CLICK HERE TO GO BACK</a></div>")
            # return HttpResponseRedirect('/you-are-logged-in/')



def home(request):
    if request.method == 'POST':
        complaint = request.POST.get('complaint')
        newidea = request.POST.get('newidea')
        upload(complaint=complaint, newidea=newidea).save()
        # id=request.session['id']
    # email=request.session['email']
    # projectdetails=request.session['projectdetails']
    # place=request.session['place']
    # funddetails=request.session['funddetails']
    # request.session['id']=id
    # request.session['projectname']=projectname
    # request.session['description']=description
    # request.session['exp']=exp
    #key = newproject.objects.all()
    #data = expenditure.objects.all()
    return render(request, 'home.html')


def cregister(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        place = request.POST.get('place')
        gender = request.POST.get('gender')
        # mp=request.POST.get('mp')
        ward = request.POST.get('ward')
        password = sha256(pass1.encode()).hexdigest()
        creg(firstname=firstname, lastname=lastname, email=email, password=password, place=place, gender=gender,
             ward=ward).save()
        return redirect('allcreg')
    return render(request, 'cregister.html')


def ngoregister(request):
    if request.method == 'POST':
        firstname = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        place = request.POST.get('place')
        mob = request.POST.get('phoneno')
        # mp=request.POST.get('mp')
        ward = request.POST.get('ward')
        password = sha256(pass1.encode()).hexdigest()
        ngoreg(name=firstname, email=email, password=password, place=place, mob=mob, ward=ward).save()
        return redirect('useruallngo')
    return render(request, 'ngoregister.html')


def app_app(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = sha256(password.encode()).hexdigest()
        user = creg.objects.filter(email=email, password=password2)
        if user:
            user_details = creg.objects.get(email=email, password=password2)
            id = user_details.id
            username_user = user_details.email
            # request.session['id']=id
            # request.session['email']=username_user
            request.session['member_id'] = id
            request.session['member_type'] = "cuser"
            request.session['name'] = user_details.firstname
            return redirect('home')
            # return redirect('home1')

    return render(request, 'councilor1login.html')


def home1(request):
    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        description = request.POST.get('description')
        exp = request.POST.get('exp')
        expenditure(projectname=projectname, description=description, exp=exp).save()
    key = newproject.objects.all()
    data = upload.objects.all()
    # if user:
    #      user_details=expenditure.objects.get(projectname=projectname,description=description,exp=exp)
    #      id=user_details.id
    #      projectname=user_details.projectname
    #      description=user_details.description
    #      exp=user_details.exp
    #      request.session['id']=id
    #      request.session['projectname']=projectname
    #      request.session['description']=description
    #      request.session['exp']=exp
    #      return redirect('home')
    # else:
    #      return redirect('login')

    # return render(request,'home1.html')
    id = request.session['id']
    email = request.session['email']
    # if request.method=='POST':
    #      firstname=request.POST.get('firstname')
    #      lastname=request.POST.get('lastname')
    #      email=request.POST.get('email')

    return render(request, 'home1.html', {'id': id, 'mail': email, 'key': key, 'data': data})


def gviews(request):
    if request.method == 'POST':
        projectdetails = request.POST.get('projectdetails')
        place = request.POST.get('place')
        funddetails = request.POST.get('funddetails')
        newproject(projectdetails=projectdetails, place=place, funddetails=funddetails).save()
    key = expenditure.objects.all()
    data = upload.objects.all()
    return render(request, 'gvtview.html', {'key': key, 'data': data})


def home2(request):
    if request.method == 'POST':
        projectdetails = request.POST.get('projectdetails')
        place = request.POST.get('place')
        funddetails = request.POST.get('funddetails')
        newproject(projectdetails=projectdetails, place=place, funddetails=funddetails).save()

        # if user:
        #      user_details=newproject.objects.get(projectdetails=projectdetails,place=place,funddetails=funddetails)
        #      projectdetails=user_details.projectdetails
        #      place=user_details.place
        #      funddetails=user_details.funddetails
        #      request.session['projectdetails']=projectdetails
        #      request.session['place']=place
        #      request.session['funddetails']=funddetails
        #      return redirect('home2')
        # else:
        #      return redirect(home2)
    return render(request, 'home2.html')


def userupload(request):
    if request.method == 'POST':
        complaint = request.POST.get('complaint')
        newidea = request.POST.get('newidea')
        upload(complaint=complaint, newidea=newidea).save()
    return render(request, 'userupload.html')


def councillorupload(request):
    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        description = request.POST.get('description')
        exp = request.POST.get('exp')
        expenditure(projectname=projectname, description=description, exp=exp).save()
    return render(request, 'councillorupload.html')


def validatepssword(s):
    l, u, p, d = 0, 0, 0, 0
    # s = "R@m@_f0rtu9e$"
    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
    specialchar = "$@_"
    digits = "0123456789"
    if (len(s) >= 8):
        for i in s:

            # counting lowercase alphabets
            if (i in smallalphabets):
                l += 1

            # counting uppercase alphabets
            if (i in capitalalphabets):
                u += 1

            # counting digits
            if (i in digits):
                d += 1

            # counting the mentioned special characters
            if (i in specialchar):
                p += 1
    if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
        return True
        # print("Valid Password")
    else:
        return False
        # print("Invalid Password")

# -------------------------------------------------------------------------------------------
