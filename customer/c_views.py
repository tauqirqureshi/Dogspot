from django.shortcuts import render,redirect
from applications.models import *
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.conf import settings
from applications.forms import RegisterFroms
from applications.forms import *
import sys
from django.utils.timezone import datetime
from datetime import date
import json 
import hashlib

from .cart import Cart_insert
# Create your views here.



# ======================  LOGIN  ==================
def login(request):
    if request.method == "POST":

        u=request.POST["email"]
        passw=request.POST["password"]
        p = hashlib.md5(passw.encode('utf')).hexdigest()
        print("sssss",p)
        val=users.objects.filter(users_email=u,users_password=p).count()
        if val==1:
            data=users.objects.filter(users_email=u,users_password=p)
            for n in data:
                request.session['customer_id']=n.users_id
                request.session['customer_email']=n.users_email
                request.session['customer_pwd']=n.users_password

                if 'cart' in request.session:
                    product_ids = request.session['cart'].keys()
                    print("----------",product_ids)
                    # product2 = products.objects.filter(products_id__in=product_ids)
                    for product in product_ids:
                        val = request.session['cart'][product]
                        count=0
                        list1=[]
                        for item in val:
                              list1.append(val[item])
                              print("++++++++++++++++++++++++++")
                              count=count+1
                              if count==4:
                                  cc1 = cart.objects.filter(products_id_id = list1[0]).count()

                                  if cc1 == 0:
                                      d  = date.today()
                                      c = cart(user_id_id = n.users_id,products_id_id = list1[0],qty=int(list1[1]),amount=int(list1[1]*list1[2]),added_date = d)
                                      c.save()
                                  else:
                                      c = cart.objects.get(products_id=list1[0])
                                      print('llllllll',c.qty)
                                      c.qty = c.qty + int(list1[1])
                                      c.save()

                    cart1 = Cart_insert(request)
                    cart1.clear()

            return redirect("/client/home")
        else:
            messages.error(request,"Invaild password and email")
            return render(request,"c-login.html")

    return render(request,"c-login.html")


def send_otp(request): 
    if request.method == "POST":
        otp1=random.randint(10000,99999)
        print(otp1)
        e=request.POST['email']
        print("----email-----",e)
        request.session['c-email']=e
        obj = users.objects.filter(users_email=e).count()

        if obj == 1:
          val = users.objects.filter(users_email=e).update(otp=otp1, otp_used=0)
          subject='OTP VERI'
          message= str(otp1)
          email_from = settings.EMAIL_HOST_USER
          recipient_list=[e]
          send_mail(subject,message,email_from,recipient_list)
          return render(request,'c-set-password.html')
    return render(request,'c-set-password.html')

def forgot(request):
    return render(request,"c-forgot.html")


def set_password(request):
    totp = request.POST['otp']
    npassword = request.POST['npass']
    cpassword = request.POST['cpass']

    if npassword == cpassword:

        e = request.session['c-email']
        val = users.objects.filter(users_email=e,otp=totp,otp_used=0).count()
        
        if val == 1:
            ps=hashlib.md5(npassword.encode('utf')).hexdigest()
            val= users.objects.filter(users_email=e).update(otp_used=1,users_password=ps)
            return redirect("/client/home")
        else:
            messages.error(request,"OTP does not match ")
            return render(request,"c-set-password.html")
    else:
        messages.error(request,"NEW PASSWORD & CONFIRM PASSWORD DEOS NOT MATCH ")
        return render(request,"c-set-password.html")
    return render(request,"c-set-password.html")

# =================  REGISTERTIONS  ==============

def register(request):
    arre=areas.objects.all()
    if request.method == "POST":
        froms=RegisterFroms(request.POST)
        
        print("===resgidskd============FROMS ERRORS",froms.errors)
        if froms.is_valid():
            newform = froms.save(commit=False)
            newform.users_password = hashlib.md5(newform.users_password.encode('utf')).hexdigest()
               
            newform.save()
            return redirect("/client/login/")
        else:
            pass
    else:
       froms=RegisterFroms()
       
    return render(request,"c-register.html",{"froms":froms,"arre":arre})

# =================  Update profile ======================================
def c_profile(request):
    cid=request.session['customer_id']
    ue=users.objects.get(users_id=cid)
    return render(request,"my-account.html",{"u":ue})

def update_c_profile(request):
    cid=request.session['customer_id']
    us=users.objects.get(users_id=cid)

    froms = cus_proFroms(request.POST,instance=us)
    
    print("===update_profile-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            froms.save()
            return redirect("/client/account/")
        except:
            print("======update_profile-from== systm====",sys.exc_info()) 
    
    return render(request,"my-account.html",{"u":us})

def pass_change(request):
    cid=request.session['customer_id']
    ue=users.objects.get(users_id=cid)

    totp = request.POST['current'] 
    npassword = request.POST['npass']
    cpassword = request.POST['cpass']

    if npassword == cpassword:
        ps=hashlib.md5(npassword.encode('utf')).hexdigest()
        val= users.objects.filter(users_id=cid).update(users_password=ps)
        return redirect("/client/account/")
       
    else:
        messages.error(request,"NEW PASSWORD & CONFIRM PASSWORD DEOS NOT MATCH ")
        return render(request,"set-password.html")


    return render(request,"my-account.html",{"u":ue})


def load_menu(request):
    c=categorys.objects.all()
    sue=sub_categorys.objects.all()
    return render(request,"c_menu.html",{"c":c,"su":sue})



def home(request):
    p2 = products.objects.all().order_by("-products_id")
    p=products.objects.all()
    p3 = products.objects.all().order_by("products_price")
    print("ssss",p3)
    return render(request,"c-index.html",{"p":p,"p2":p2,"p3":p3})

def select_sub_category(request,sub_categorys_id):
    c=categorys.objects.all()
    su=sub_categorys.objects.all()
    ga=products.objects.filter(sub_categorys_id=sub_categorys_id)
    return render(request,"shop-sidebar.html",{"ga":ga,"c":c,"su":su})    

def select_category(request,categorys_id):
    c=categorys.objects.all()
    su=sub_categorys.objects.all()
    gsa=sub_categorys.objects.filter(categorys_id=categorys_id)
    ga=products.objects.filter(sub_categorys_id__in=gsa)
    print('ooooooooooooooooo',ga)
    return render(request,"shop-sidebar.html",{"ga":ga,"c":c,"su":su})

def product_details(request,products_id):
    p=products.objects.filter(products_id=products_id)
    c=gallerys.objects.all().filter(products_id=products_id)
    
    feed=feedbacks.objects.filter(products_id=products_id)
    sql1="SELECT products_id_id as feedbacks_id , FLOOR(AVG(rate)) as AVG FROM feedbacks GROUP by products_id_id"
    q=feedbacks.objects.raw(sql1)

    for k in p:
        o=k.sub_categorys_id.sub_categorys_id

    newp=products.objects.filter(sub_categorys_id=o)
    print("ooooooooooooooooooooo",newp)
    return render(request,"product-details.html",{"p":p,"g":c,"fee":feed,"sqlrate":q,"newp":newp})



def checkout(request):
    u_id=request.session['customer_id']
    user=users.objects.filter(users_id=u_id)
    for h in user:
        print("ddddddd",h.areas_id.areas_id)
        r=h.areas_id.areas_id
    carts=cart.objects.filter(user_id=u_id)
    are=areas.objects.filter(areas_id=r)
    sum = 0
    for val in carts:
        sum = sum + (val.amount * val.qty)
    print("----------", sum)
    return render(request,"checkout.html",{"c":carts,"a":are,"u":user,"total":sum})

def wishlist(request):
    idd= request.session['customer_id']
    wish=wishlists.objects.filter(users_id=idd)
    return render(request,"wishlist.html",{"wish":wish}) 


def feedback(request,products_id):
    idd= request.session['customer_id']
    us=users.objects.filter(users_id=idd)
    for i in us:
        o=i.users_id
        print("----",i.users_id)
    try:
        da=datetime.today()
        pro_id=products_id
        des=request.POST['message']
        ratep=request.POST['rate']
        uid=o
        print("-----",uid,da,pro_id,des)
        f=feedbacks(suggestion_date=da,users_id_id=uid,suggestion=des,products_id_id=pro_id,rate=ratep)
        f.save()
        return redirect("/client/product-details/%s"%pro_id)
    except:
        print("=====feedback=======",sys.exc_info())
    return redirect("/client/product-details/%s"%pro_id)




def sidebar(request):
    c=categorys.objects.all()
    su=sub_categorys.objects.all()

    if request.method=="POST":
        name = request.POST["products_name"]
        ga=products.objects.filter(products_name= name)
    else:
        ga=products.objects.all()
    return render(request,"shop-sidebar.html",{"ga":ga,"c":c,"su":su})    
    



def cart_(request):
    if 'customer_id' in request.session:
        id_c=request.session['customer_id']
        c=cart.objects.filter(user_id_id=id_c)
        sum = 0
        for val in c :
            sum = sum + (val.amount * val.qty)
        print("----------", sum)
        return render(request,"cart.html",{"cartd":c,"total":sum})
    else:
        carts = Cart_insert(request)
        total = carts.get_total_price()
        print(total)
        return render(request,"cart.html",{"total":total}) 

def cart_menu(request):
    if 'customer_id' in request.session:
        u_id=request.session['customer_id']
        ca=cart.objects.filter(user_id=u_id)
        sum = 0
        for val in ca :
            sum = sum + (val.amount * val.qty)
        print("----------", sum)
        return render(request,"cart_menu.html",{"ca":ca,"total":sum})
    else:
        carts = Cart_insert(request)
        total = carts.get_total_price()
        print(total)
        return render(request,"cart_menu.html",{"total":total})  







def docter_details(request):
    d=docters.objects.all()
    return render(request,"docter_details.html",{"d":d})



def clogout(request):
    try:
        del request.session['customer_id']
        del request.session['customer_email']
        del request.session['customer_pwd']
        return redirect("/client/login/")
    except:
        pass
    return redirect("/client/home/")



def insert_cart(request,products_id):
    
    print("inside cart function")
    if 'customer_id' in request.session:
    
            try:
                u=request.session["customer_id"]
                qty=request.POST["quantity"]
                p=request.POST["amt"]
                d=date.today().strftime("%Y-%m-%d")
                print("-------------",u,qty,p,d)
                C=cart(user_id_id=u,products_id_id=products_id,qty=qty,amount=p,added_date=d)
                C.save()
            except:
                print("-------", sys.exc_info())
            return redirect('/client/cart')
    else:
        try:

            qty = request.POST['quantity']
            # d = date.today()
            # prd_id = request.POST['products_id']
            # prd_name = request.POST['products_name']
            # amt = request.POST['amt']
            # total = int(qty) * int(amt)

            cartss=Cart_insert(request)
            print("+++++++++++++++++",cartss)
            product=products.objects.get(products_id=products_id)
            print(product)
            cartss.add(Product=product, quantity=int(qty))
            print(cartss)



            # c = cart(qty = qty,amount = total,added_date=d,products_id_id=prd_id,user_id_id=1)
            # c.save()
        
        except:
            print("-------",sys.exc_info())

    return redirect('/client/cart/')


def destroy_cart(request,id):
    if 'customer_id' in request.session:
        pro=cart.objects.filter(products_id=id)
        pro.delete()
        return redirect("/client/cart/")
    else:    
        cartt=Cart_insert(request)
        produc=products.objects.get(products_id=id)
        print('dddd',produc.products_id)
        cartt.remove(produc)
        return redirect("/client/cart/")
       


def clear_cart(request):
    if 'customer_id' in request.session :
        u=request.session["customer_id"]
        c=cart.objects.filter(user_id=u)
        c.delete()
        return redirect("/client/carts")
    else:
        cartt=Cart_insert(request)
        cartt.clear()
        return redirect("/client/cart/")



def add_wishlist(request,id):
    if 'customer_id' in request.session :
        d=date.today()
        pro_id=id
        userid=request.session['customer_id']

        obj=wishlists(added_date=d,products_id_id=pro_id,users_id_id=userid)
        obj.save()
        return redirect('/client/wishlist/')

    else:
        return redirect("/client/login/")


def int_wishlist(request):
    if 'customer_id' in request.session :
        if request.method == "POST":
            try:
                d=date.today()
                pro_id=request.POST['products_id']
                userid=request.session['customer_id']

                obj=wishlists(added_date=d,products_id_id=pro_id,users_id_id=userid)
                obj.save()
                return redirect('/client/wishlist/')
            except:
                print("======Wish list ==================",sys.exc_info())
        else:
            return redirect("/client/product-details/%s"%pro_id) 
    else:
        return redirect("/client/login/")

def wishlist_delete(request,wishlists_id):
    wi=wishlists.objects.filter(wishlists_id=wishlists_id)
    wi.delete()
    return redirect('/client/wishlist/')



def autosuggest(request):
    if 'term' in request.GET:
        qs=products.objects.filter(products_name__instartswith=request.GET.get('term'))

        name=list()

        for x in qs:
            name.append(x.products_name)
        
        return JsonResponse(name,safe=False)
    return render(request,"c-header-footer.html")


def sort_products(request):
    sid=request.GET.get('sort')
    print("---- SORT 000000000000",sid)

    if sid == '1':
        p = products.objects.all().order_by("products_name")
    elif sid == '2':
        p = products.objects.all().order_by("-products_name")
    elif sid == '3':
        p = products.objects.all().order_by("products_price")    
    elif sid == '4':
        p = products.objects.all().order_by("-products_price")
    elif sid == '0':
        p = products.objects.all()

    return render(request,"sort.html",{"ga":p})


def filter_price(request):
    s=request.GET.get('start')
    e=request.GET.get('end')
    print("-------------",s)
    print("-------------",e)
    p=products.objects.filter(products_price__range=[int(s),int(e)])
    return render(request,"sort.html",{"ga":p})


def select_checkout(request,total):
    if request.session.has_key('customer_id'):
        amt = total
        print(amt)
        uid = request.session['customer_id']
        date1 = date.today().strftime("%Y-%m-%d")
        o = orders(users_id_id=uid, total_amount=int(amt), orders_date=date1,payments_status=0, orders_status=0)
        o.save()
        id = orders.objects.latest('orders_id')
        print("--------------------order id--", id)
        c = cart.objects.filter(user_id=uid)

        flag = 0
        for data in c:
            pid = data.products_id_id
            qty = data.qty
            pri = data.amount
            total=int(qty)*pri
            print("0000000000000000000000000000000000",total)
            o = order_items(order_quantity=int(qty), products_id_id=pid, orders_id_id=id.orders_id, order_amount=pri ,oreder_total=total)
            o.save()

        c_delete = cart.objects.filter(user_id=uid)
        c_delete.delete()
        return redirect("/client/order/")
        
    return render(request, "checkout.html")
        
def select_payment(request,total):
    if request.session.has_key('customer_id'):
        amt = total
        print(amt)
        uid = request.session['customer_id']
        date1 = date.today().strftime("%Y-%m-%d")
        o = orders(users_id_id=uid, total_amount=int(amt), orders_date=date1,payments_status=1, orders_status=0)
        o.save()
        id = orders.objects.latest('orders_id')
        print("--------------------order id--", id)
        c = cart.objects.filter(user_id=uid)

        flag = 0
        for data in c:
            pid = data.products_id_id
            qty = data.qty
            pri = data.amount
            total=int(qty)*pri
            print("0000000000000000000000000000000000",total)
            o = order_items(order_quantity=int(qty), products_id_id=pid, orders_id_id=id.orders_id, order_amount=pri ,oreder_total=total)
            o.save()

        c_delete = cart.objects.filter(user_id=uid)
        c_delete.delete()
        return redirect("/client/order/")

    return render(request, "checkout.html")


def cancel(request):
    return render(request,'cancel.html')



def order_(request):
    uid = request.session['customer_id']
    ord=orders.objects.filter(users_id=uid)
    return render(request,"orderss.html",{"ord":ord})


def order_details(request,orders_id):
    order_item=order_items.objects.filter(orders_id=orders_id)
    return render(request,"orderDetails.html",{"order":order_item})


def update_cart(request,id):
    if 'customer_id' in request.session:
        qtye=request.GET.get('qty')

        val=cart.objects.get(cart_id=id)
        new_qty=int(qtye)
        val=cart.objects.filter(cart_id=id).update(qty=new_qty)
    else:
        c=Cart_insert(request)
        p=products.objects.get(products_id=id)
        print(p)
        qty=request.GET.get('qty')
        c.add(Product=p,quantity=int(qty),update_quantity=True)
        print(c)
    return redirect("/client/cart/")