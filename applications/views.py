from django.shortcuts import render,redirect,HttpResponse
from applications.models import *
from django.core.mail import send_mail
import sys
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings 
from applications.forms import *
from applications.functions import handle_uploaded_file
from django.contrib import messages
# ==========g======================
from django.db import connection
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.cache import cache_control

class HomeView(View):
    def get(self,request,*agrs,**kwargs):
        return render(request,"index2.html") 


class ProjectChart(APIView):
    authentication_classes =[]
    permission_classes=[]

    def get(self,request,format=None):
        cursor=connection.cursor()
        cursor.execute('''SELECT (select products_name  from products where products_id = i.products_id_id) as name  , count(*) as total FROM `orderitems` i join products p where i.products_id_id = p.products_id GROUP by i.products_id_id''') 
        qs=cursor.fetchall()
        print("==============")
        labels=[]
        default_items=[]
        for item in qs:
            labels.append(item[0])
            default_items.append(item[1])
        
        data={
            "labels":labels,
            "default":default_items,
        }
        return Response(data)

 
# ------------_____Selete_QUERY____----------------------
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def user_table(request):
    user=users.objects.all()
    if header(request):
        return render(request,"user-table.html",{'user':user})
    else:
        return redirect("/admin-login/")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def state_table(request):
    state=states.objects.all()
    if header(request):
        return render(request,"state-table.html",{'state':state})
    else:
        return redirect("/admin-login/")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def city_table(request):
    city=citys.objects.all()
    state=states.objects.all()
    if header(request):
        return render(request,"city-table.html",{"city":city,"s":state})
    else:
        return redirect("/admin-login/")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def area_table(request):
    # area=areas.objects.all().select_related('citys_id')
    area=areas.objects.all()
    c=citys.objects.all()
    if header(request):
        return render(request,"area-table.html",{'area':area,})
    else:
        return redirect("/admin-login/")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def category_table(request):
    category=categorys.objects.all()
    if header(request):
        return render(request,"category-table.html",{'category':category})
    else:
        return redirect("/admin-login/")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def sub_category_table(request):
    sub_category=sub_categorys.objects.all()
    if header(request):
        return render(request,"sub-category-table.html",{'sub_category':sub_category})
    else:
        return redirect("/admin-login/")    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def product_table(request):
    product=products.objects.all()
    if header(request):
        return render(request,"product-table.html",{'product':product})
    else:
        return redirect("/admin-login/")    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def payment_table(request):
    payment=payments.objects.all()
    if header(request):
        return render(request,"payment-table.html",{'payment':payment})
    else:
        return redirect("/admin-login/")    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def order_table(request):
    order=orders.objects.all()
    if header(request):
        return render(request,"order-table.html",{'order':order})
    else:
        return redirect("/admin-login/")    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def wishlist_table(request):
    wish=wishlists.objects.all()
    if header(request):
        return render(request,"wishlist-table.html",{"wish":wish}) 
    else:
        return redirect("/admin-login/")    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def gallery_table(request):
    gallery=gallerys.objects.all()
    if header(request):
        return render(request,"gallery-table.html",{'gallery':gallery})
    else:
        return redirect("/admin-login/")    


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def docter_table(request):
    docter=docters.objects.all()
    if header(request):
        return render(request,"docter-table.html",{'docter':docter})
    else:
        return redirect("/admin-login/")    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def order_items_table(request,orders_id):
    order_item=order_items.objects.filter(orders_id=orders_id)
    if header(request):
        return render(request,"order-item-table.html",{'order_item':order_item})
    else:
        return redirect("/admin-login/")    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def feedback_table(request):
    feedback=feedbacks.objects.all()
    if header(request):
        return render(request,"feedback-table.html",{"feedback":feedback})
    else:
        return redirect("/admin-login/")    

#----------------------------------------------------------------
#__________--------DELETE _ columns --------__________________________
#-----------------------------------------------------------------
def delete_state(request,states_id):
    state_d=states.objects.get(states_id=states_id)
    state_d.delete()
    return redirect("/state-table")

def delete_city(request,citys_id):
    city_d=citys.objects.get(citys_id=citys_id)
    city_d.delete()
    return redirect("/city-table")

def delete_area(request,areas_id):
    area_d=areas.objects.get(areas_id=areas_id)
    area_d.delete()
    return redirect("/area-table")

def delete_category(request,categorys_id):
    category_d=categorys.objects.get(categorys_id=categorys_id)
    category_d.delete()
    return redirect("/category-table")

def delete_sub_category(request,sub_categorys_id):
    sub_category_d=sub_categorys.objects.get(sub_categorys_id=sub_categorys_id)
    sub_category_d.delete()
    return redirect("/sub-category-table")

def delete_product(request,products_id):
    product_d=products.objects.get(products_id=products_id)
    product_d.delete()
    return redirect("/product-table")

def delete_payment(request,payments_id):
    payment_d=payments.objects.get(payments_id=payments_id)
    payment_d.delete()
    return redirect("/payment-table")
    
def delete_order(request,orders_id):
    order_d=orders.objects.get(orders_id=orders_id)
    order_d.delete()
    return redirect("/order-table")

def delete_gallery(request,gallerys_id):
    gallery_d=gallerys.objects.get(gallerys_id=gallerys_id)
    gallery_d.delete()
    return redirect("/gallery-table")

def delete_docter(request,docters_id):
    docter_d=docters.objects.get(docters_id=docters_id)
    docter_d.delete()
    return redirect("/docter-table")

def delete_order_item(request,order_items_id):
    order_item_d=order_items.objects.get(order_items_id=order_items_id)
    order_item_d.delete()
    o=order_items_id
    return redirect("/order-table/")

def delete_feedback(request,feedbacks_id):
    feedback_d=feedbacks.objects.get(feedbacks_id=feedbacks_id)
    feedback_d.delete()
    return redirect("/feedback-table")
# +++++++++++++++++++++++   END  +++++++++++++++++++++++++++++


#----------------------------------------------------------------
#__________--------Admin _ Login --------__________________________
#-----------------------------------------------------------------
def admin_login(request):
    if request.method == "POST":
       e = request.POST["email"]
       p = request.POST["password"]
       print(" ????????????? ")

       val = users.objects.filter(users_email=e, users_password=p, is_admin=1 ).count()
       print(" --------------- ")
       if val==1:
           date=users.objects.get(users_email=e,users_password=p)
        
           request.session['admin_id']=date.users_id
           request.session['admin_email']=date.users_email
           
           return redirect('/index/')
       else:    
           messages.error(request,"Invaild password and email")
           return render(request,"admin-login.html")
    else:
               
       return render(request,"admin-login.html")

# =======================
#  profile edit
# ==========================================
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def edit_profile(request):
    if header(request):
        id=request.session['admin_id']
        us=users.objects.get(users_id=id)
        
        return render(request,"profile.html",{"us":us})
    else:
        return redirect("/admin-login/")

    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def update_profile(request):
    id=request.session['admin_id']
    us=users.objects.get(users_id=id)
    froms=userFroms(request.POST,instance=us)
    
    print("===update_profile-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            froms.save()
            return redirect("/user-table")
        except:
            print("======update_profile-from== systm====",sys.exc_info()) 
    if header(request):
        return render(request,"profile.html",{"us":us})
    else:
        return redirect("/admin-login/")








def forgot(request):
    return render(request,"admin-forgot-password.html")



def send_OTP(request):

    if request.method == "POST":
        otp1=random.randint(10000,99999)
        print(otp1)
        e=request.POST['email']
        print("----email-----",e)
        request.session['temail']=e
        obj = users.objects.filter(users_email=e).count()

        if obj == 1:
          val = users.objects.filter(users_email=e).update(otp=otp1, otp_used=0)
          subject='your dogspot verifications  OTP  '
          message= str(otp1)
          email_from = settings.EMAIL_HOST_USER
          recipient_list=[e,]
          send_mail(subject,message,email_from,recipient_list)
          return render(request,'set-password.html')
    return render(request,'admin-forgot-password.html')

def set_password(request):
    totp = request.POST['otp'] 
    npassword = request.POST['npass']
    cpassword = request.POST['cpass']

    if npassword == cpassword:

        e = request.session['temail']
        val = users.objects.filter(users_email=e,otp=totp,otp_used=0).count()
        
        if val == 1:
            val= users.objects.filter(users_email=e).update(otp_used=1,users_password=npassword)
            return redirect("/admin-login/")
        else:
            messages.error(request,"OTP does not match ")
            return render(request,"set-password.html")
    else:
        messages.error(request,"NEW PASSWORD & CONFIRM PASSWORD DEOS NOT MATCH ")
        return render(request,"set-password.html")
    return render(request,"set-password.html")
    

# +++++++++++++++++++++++   END  +++++++++++++++++++++++++++++






#----------------------------------------------------------------
#__________--------Insert _ columns --------__________________________
#-----------------------------------------------------------------
def insert_category(request):
    if request.method == "POST":
        froms=categoryForms(request.POST)
        print("===category============FROMS ERRORS",froms.errors)
        if froms.is_valid():
            froms.save()
            return redirect("/category-table/")
        else:
            pass
    else:
       froms=categoryForms()

    return render(request,"insert-category.html",{"froms":froms})

 

        

def insert_sub_category(request):
    category = categorys.objects.all()
    if request.method =="POST":
        froms= sub_categoryForms(request.POST)
        print("===sub category ============FROMS ERRORS",froms.errors)
        if froms.is_valid():
            froms.save()
            return redirect("/sub-category-table")
        else:
            pass
    else:
        froms=sub_categoryForms()
    
    return render(request,"insert-sub-category.html",{"froms":froms,"category":category})

def insert_state(request):
    if request.method == "POST":
        froms = stateForms(request.POST)
        print("===state ============FROMS ERRORS",froms.errors)
        if froms.is_valid():
            froms.save()
            return redirect("/state-table")
        else:
            pass
    else:
        froms=stateForms()

    return render(request,"insert-state.html",{"froms":froms})


def insert_city(request):
    state = states.objects.all()
    if request.method == "POST":
        froms = cityForms(request.POST)
        print("===city============FROMS ERRORS",froms.errors)
        if froms.is_valid():
            froms.save()
            return  redirect("/city-table",)
        else:
            pass
    else:
        froms = cityForms()
    return render(request,"insert-city.html",{"froms":froms,"state":state})

def insert_area(request):
    city=citys.objects.all()
    if request.method == "POST":
        froms = areaForms(request.POST)
        print("===area============FROMS ERRORS",froms.errors)
        if froms.is_valid():
            froms.save()
            return redirect("/area-table")
        else:
            pass
    else:
        froms= areaForms()
        city=citys.objects.all()
    return render(request,"insert-area.html",{"froms":froms,"city":city}) 

def insert_docter(request):
    if request.method == "POST":
        forms=docterForms(request.POST,request.FILES)
        print("==Docter============FROMS ERRORS",forms.errors)
        if forms.is_valid():
            handle_uploaded_file(request.FILES['docters_image'])
            forms.save()
            return redirect("/docter-table")
        else:
            pass
    else:
        forms= docterForms()
        
    return render(request,"insert-docter.html",{"forms":forms}) 
      
def insert_product(request):
    sub_cate=sub_categorys.objects.all()
    
    if request.method == "POST":
        forms = productForms(request.POST,request.FILES)
        print("==PRODUCT============FROMS ERRORS",forms.errors)
        if forms.is_valid():
            handle_uploaded_file(request.FILES['products_image'])
            forms.save()
            return redirect("/product-table")
        else:
            pass
    else:
        forms = productForms()
    return render(request,"insert-product.html",{"forms":forms,"sub_cate":sub_cate})
        
def insert_gallery(request):
    product = products.objects.all()
    if request.method=="POST":
        forms = galleryFroms(request.POST,request.FILES)
        print("===================",forms.errors)
        if forms.is_valid():
            handle_uploaded_file(request.FILES['images'])
            forms.save()
            return redirect('/gallery-table/')
        else:
            pass
    else:
        forms=galleryFroms()
        return render(request,'insert-gallery.html',{"product":product})


# ======= UPDATE -  TABLE =================================

# ===state table====
def eidt_state(request,states_id):
    s=states.objects.get(states_id=states_id)
    return render(request,"update-state.html",{"s":s})

def update_state(request,states_id):
    s=states.objects.get(states_id=states_id)

    froms=stateForms(request.POST,instance=s)
    print("===update_state-from== errors====",froms.errors)

    if froms.is_valid():
        try:
            froms.save()
            return redirect("/state-table")
        except:
            print("======update_state-from== systm====",sys.exc_info()) 
    return render(request,"update-state.html")


# ===city table====
def edit_city(request,citys_id):
    c=citys.objects.get(citys_id=citys_id)
    s=states.objects.all()

    return render(request,"update-city.html",{"c":c,"s":s}) 

def update_city(request,citys_id):
    c=citys.objects.get(citys_id=citys_id)
    

    froms=cityForms(request.POST,instance=c)
    print("===update_citys-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            froms.save()
            return redirect("/city-table")
        except:         
            print("======update_state-from== systm====",sys.exc_info())
    s=states.objects.all()
    return render(request,"update-city.html",{"c":c,"s":s})

# ===city table====
def edit_area(request,areas_id):
    a=areas.objects.get(areas_id=areas_id)
    c=citys.objects.all()

    return render(request,"update-area.html",{"a":a,"c":c})

def update_area(request,areas_id):
    a=areas.objects.get(areas_id=areas_id)
    
    froms=areaForms(request.POST,instance=a)
    print("===update_citys-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            froms.save()
            return redirect("/area-table")
        except:
            print("======update_state-from== systm====",sys.exc_info())
    c=citys.objects.all()
    return render(request,"update-area.html",{"a":a,"c":c})

# ===============================categorys update=================================================
def edit_category(request,categorys_id):
    cate=categorys.objects.get(categorys_id=categorys_id)
    return render(request,"update-category.html",{"cate":cate})

def update_categorys(request,categorys_id):
    cate=categorys.objects.get(categorys_id=categorys_id)

    froms=categoryForms(request.POST,instance=cate)
    print("===update-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            froms.save()
            return redirect("/category-table")
        except:
            print("======update_state-from== systm====",sys.exc_info())
    return render(request,"update-category.html",{"cate":cate})
# =============================== sub categorys update=================================================

def edit_sub_category(request,sub_categorys_id):   
    s=sub_categorys.objects.get(sub_categorys_id=sub_categorys_id)
    c=categorys.objects.all()
    return render(request,"update-sub-category.html",{"s":s,"c":c})

def update_sub_category(request,sub_categorys_id):
    s=sub_categorys.objects.get(sub_categorys_id=sub_categorys_id)
    
    froms=sub_categoryForms(request.POST,instance=s)
    print("===update_citys-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            froms.save()
            return redirect("/sub-category-table")
        except:
            print("================",sys.exc_info())

    c=categorys.objects.all()
    return render(request,"update-sub-category.html",{"s":s,"c":c})

# =============================== product update=================================================
def edit_product(request,products_id):
    p=products.objects.get(products_id=products_id)
    s=sub_categorys.objects.all()
    return render(request,"update-product.html",{"p":p,"s":s})

def update_product(request,products_id):
    p=products.objects.get(products_id=products_id)
    
    froms=productForms(request.POST,request.FILES,instance=p)
    print("===update_products-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            handle_uploaded_file(request.FILES['products_image'])
            froms.save()
            return redirect("/product-table")
        except:
            print("================",sys.exc_info())

    s=sub_categorys.objects.all()
    return render(request,"update-product.html",{"p":p,"s":s})


# =============================== gallery update==================================
def edit_gallery(request,gallerys_id):
    g=gallerys.objects.get(gallerys_id=gallerys_id)
    p=products.objects.all()
    return render(request,"update-gallery.html",{"g":g,"p":p})

def update_gallery(request,gallerys_id):
    g=gallerys.objects.get(gallerys_id=gallerys_id)
    
    froms= galleryFroms(request.POST, request.FILES, instance=g)
    print("===update_products-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            handle_uploaded_file(request.FILES['images'])
            froms.save()
            return redirect("/gallery-table")
        except:
            print("================",sys.exc_info())

    p=products.objects.all()
    return render(request,"update-gallery.html",{"g":g,"p":p})



# =============================== docter update=================================================
def edit_docter(request,docters_id):
    d=docters.objects.get(docters_id=docters_id)
    return render(request,"update-docter.html",{"d":d})

def update_docter(request,docters_id):
    d=docters.objects.get(docters_id=docters_id)
    
    froms=docterForms(request.POST,request.FILES,instance=d)
    print("===update_docter-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            handle_uploaded_file(request.FILES['docters_image'])
            froms.save()
            return redirect("/docter-table")
        except:
            print("================",sys.exc_info())
    else:
        pass

    return render(request,"update-docter.html",{"d":d})



# ========================================

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def index(request):
    user=users.objects.all().count()
    order = orders.objects.all().count()
    order_item=order_items.objects.all().count()
    product=products.objects.all().count()
    u=users.objects.all()
    if header(request):
        return render(request,"index2.html",{"user":user,"order":order,"order_item":order_item,"product":product,"u":u})
    else:
        return render(request,"admin-login.html")

def appect_order(request,orders_id):
    val= orders.objects.filter(orders_id=orders_id).update(orders_status=1)
    return redirect("/order-table/")


def reject_order(request,orders_id):
    val= orders.objects.filter(orders_id=orders_id).update(orders_status=2)
    return redirect("/order-table/")

def alogout(request):
    try:
        del request.session['admin_id']
        del request.session['admin_email']
        
    except:
        pass
    return render(request,"admin-login.html")


def header(request):
    if request.session.has_key('admin_id'):
        return True
    else:
        return False

@csrf_exempt
def order_repost(request):
    order=orders.objects.all()
    pro=products.objects.all()

    if request.method=="POST":
        key=request.POST.get('product')
        print(key)
        print(type(key))
        sql="SELECT * FROM `orders` o join orderitems i join products p join sub_categorys s where o.orders_id = i.orders_id_id and i.products_id_id = p.products_id and p.sub_categorys_id_id = s.sub_categorys_id and p.sub_categorys_id_id = %s"
        d=orders.objects.raw(sql,[key])
        return render(request,"order_repost2.html",{"order":d})
    else:
        return render(request,"order_repost.html",{'order':order,"produc":pro})

def repost2(request):
    order=orders.objects.all()

    if request.method == "POST":

        start = request.POST["start"]
        end = request.POST["end"]
        start = parse_date(start)
        end = parse_date(end)
        if start<end:

            print("--s--",start,"-----e----",end)

            que = orders.objects.filter(orders_date__range=[start,end])
            return render(request,"repost.html",{"order": que})
        else:
            # order=orders.objects.all()
            msg=messages.error(request,"ksksksksksk")
            return render(request,"repost.html",{"order": order,"msg":msg})

    return render(request,"repost.html",{'order':order})


def repost3(request):
    sql33="SELECT (select users_email from users where users_id = o.users_id_id) as name, sum(total_amount) as orders_id FROM `orders` o join users u WHERE o.users_id_id = u.users_id group by o.users_id_id "
    order=orders.objects.raw(sql33)
    return render(request,"repost3.html",{'order':order})


def client(request):
    return redirect("/client/home/")