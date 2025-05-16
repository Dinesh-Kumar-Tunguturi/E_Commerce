from django.shortcuts import render,redirect
from django.http import HttpResponse
from Shop.models.product import Product
from Shop.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from Shop.models.customer import Customer
from django.views import View


# class based view
class home(View):
    def get(self,request):
        categories=Category.objects.all()
        CategoryID=request.GET.get('category')
        if CategoryID:
            products=Product.get_category_id(CategoryID)
        else:
            products=Product.objects.all()
        data={'products':products, 'categories':categories}
        return render(request, 'index.html', data)


    def post(self,request):
        pass

