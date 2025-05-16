from django.shortcuts import render,redirect
from django.http import HttpResponse
from Shop.models.product import Product
from Shop.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from Shop.models.customer import Customer
from django.views import View


# class based view
class login(View):
    def get(self, request):
        return render(request,'login.html')
    def post(self, request):
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

