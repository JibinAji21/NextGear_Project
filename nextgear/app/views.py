from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid username or password")
            return redirect(shop_login)
    else:
        return render(req,'login.html')
    
def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(shop_login)
    
def shop_home(req):
    if 'shop' in req.session:
        product=Product_category.objects.all()
        return render(req,'shop/shop_home.html',{'products':product})
    else:
        return redirect(shop_login)
    
def product_categories(req,id):
    category = Product_category.objects.get(id=id)
    product_details = Product.objects.filter(category=category)
    return render(req, 'shop/productlist.html', {'category': category,'product_details':product_details})



