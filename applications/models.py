from django.db import models

# # Create your models here.
 #  1  tables
class states(models.Model):
    states_id = models.AutoField(primary_key=True)
    states_name = models.CharField(null=False,max_length=50)
    class Meta:
        db_table = "states"


 # 2 tables
class citys(models.Model):
    citys_id = models.AutoField(primary_key=True)
    citys_name = models.CharField(null=False, max_length=30)
    states_id = models.ForeignKey(states,on_delete=models.PROTECT)
    class Meta:
        db_table = "citys"


 # 3 tables
class areas(models.Model):
    areas_id = models.AutoField(primary_key=True)
    areas_name = models.CharField(null=False, max_length=30)
    citys_id = models.ForeignKey(citys, on_delete=models.PROTECT)
    class Meta:
        db_table = "areas"


 # 4 tables
class users(models.Model):
    users_id = models.AutoField(primary_key=True)
    users_address = models.CharField(null=False, max_length=500)
    users_password = models.CharField(null=False, max_length=150)
    users_email = models.EmailField(null=False, max_length=150)
    mobile_no = models.BigIntegerField(null=False)
    birth_of_date = models.DateField(null=False)
    first_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    areas_id = models.ForeignKey(areas, on_delete=models.PROTECT)
    is_admin = models.IntegerField()
    otp = models.CharField(max_length=10,null=True)
    otp_used = models.IntegerField()
    # otp=models.IntegerField()
    class Meta:
        db_table = "users"


 # 5 tables
class categorys(models.Model):
    categorys_id = models.AutoField(primary_key=True)
    categorys_name = models.CharField(null=False, max_length=50)
    class Meta:
        db_table = "categorys"

    
 # 6 tables
class sub_categorys(models.Model):
    sub_categorys_id = models.AutoField(primary_key=True)
    sub_categorys_name = models.CharField(null=False, max_length=50)
    categorys_id = models.ForeignKey(categorys, on_delete=models.PROTECT)
    class Meta:
        db_table = "sub_categorys"


 # 7 tables
class products(models.Model):
    products_id = models.AutoField(primary_key=True)
    products_name = models.CharField(null=False, max_length=150)
    products_image= models.CharField(null=False, max_length=150)
    products_price = models.IntegerField(null=False,)
    products_quantity = models.IntegerField(null=False)
    products_description = models.CharField(max_length=200)
    sub_categorys_id = models.ForeignKey(sub_categorys, on_delete=models.PROTECT)
    class Meta:
        db_table = "products"


 # 8 tables
class payments(models.Model):
    payments_id = models.AutoField(primary_key=True)
    payments_types = models.CharField(null=False, max_length=20)
    class Meta:
        db_table = "payments"

 # 9 tables
class orders(models.Model):
    orders_id = models.AutoField(primary_key=True)
    orders_date = models.DateField(null=False)
    total_amount = models.FloatField(null=False)
    users_id = models.ForeignKey(users, on_delete=models.PROTECT)
    orders_status=models.IntegerField()
    payments_status=models.IntegerField()
    class Meta:
        db_table = "orders"





 # 10 tables
class gallerys(models.Model):
    gallerys_id = models.AutoField(primary_key=True)
    images = models.CharField(null=False, max_length=150)
    products_id = models.ForeignKey(products,on_delete=models.PROTECT)
    class Meta:
        db_table = "gallery"


# 11 tables
class docters(models.Model):
    docters_id = models.AutoField(primary_key=True)
    docters_image = models.CharField(null=False, max_length=250)
    docters_name = models.CharField(null=False, max_length=50)
    docters_no = models.IntegerField(null=False)
    hospital_name = models.CharField(max_length=50)
    hospital_no = models.IntegerField(null=False)
    hospital_address = models.CharField(null=False, max_length=250)
    class Meta:
        db_table = "docters"


# 12 tables
class order_items(models.Model):
    order_items_id = models.AutoField(primary_key=True)
    orders_id = models.ForeignKey(orders, on_delete=models.PROTECT)
    order_quantity=models.IntegerField(null=False)
    order_amount=models.IntegerField()
    oreder_total=models.IntegerField()
    products_id = models.ForeignKey(products,on_delete=models.PROTECT)
    class Meta:
        db_table = "orderitems"


# # 13 tables
class feedbacks(models.Model):
    feedbacks_id = models.AutoField(primary_key=True)
    suggestion_date = models.DateField(null=False)
    users_id = models.ForeignKey(users, on_delete=models.PROTECT)
    suggestion = models.CharField(null=False, max_length=200)
    rate = models.IntegerField(5)
    products_id = models.ForeignKey(products, on_delete=models.PROTECT)
    class Meta:
        db_table = "feedbacks"

class cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(users, on_delete=models.PROTECT)
    products_id = models.ForeignKey(products, on_delete=models.PROTECT)
    qty=models.IntegerField()
    amount=models.IntegerField()
    added_date=models.DateField()
    class Meta:
        db_table = "carts"


class wishlists(models.Model):
    wishlists_id=models.AutoField(primary_key=True)
    users_id=models.ForeignKey(users, on_delete=models.PROTECT)
    products_id = models.ForeignKey(products, on_delete=models.PROTECT)
    added_date=models.DateField()
    class Meta:
        db_table = "wishlists"



