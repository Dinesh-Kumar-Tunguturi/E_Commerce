from django.shortcuts import render,redirect
from django.http import HttpResponse
from .product import Product
from .category import Category
from django.contrib.auth.hashers import make_password,check_password
from .customer import Customer


def signup(request):
    if request.method == 'GET':

        return render(request, "signup.html")
    else:
        fn=request.POST['fn']
        ln=request.POST['ln']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        
        userdata=[fn,ln,email,password,mobile]
        print(userdata)

        uservalues={
            'fn':fn,
            'ln':ln,
            'email':email,
            'mobile':mobile,
            'password':password
        }
        customerdata=Customer(first_name=fn, last_name=ln, email=email,mobile=mobile,password=password)
        # validation
        error_msg=None
        success_msg=None
        if(not fn):
            error_msg="First Name should Not be empty"
        elif(not ln):
            error_msg="Last Name should Not be empty"
        elif(not email):
            error_msg="email field Not be empty"
        elif(not mobile):
            error_msg="mobile number should Not be empty"
        elif(not password):
            error_msg="Password field should Not be empty"
        elif(customerdata.isexit()):
            error_msg="Email already Exist."
        if (not error_msg):
            customerdata.password=make_password(customerdata.password)
            success_msg="Account created successfully"
            customerdata.save()
            msg={'success':success_msg}
            return render(request, 'signup.html', msg)
        else:
            msg={'error': error_msg,'value':uservalues}
            return render(request, 'signup.html', msg)
        


# login page 
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
        # to check email found or not
        users=Customer.getemail(email)
        error_msg=None
        if users:
            # if email found check password
            check=check_password(password,users.password)
            if check:
                return redirect('/')
            else:
                error_msg="Password is incorrect"
                msg={'error':error_msg}
                return render(request,'login.html', msg)
        else:
            error_msg="Email is incorrect"
            msg={'error':error_msg}
            return render(request,'login.html', msg)

