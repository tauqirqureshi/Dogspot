from django import forms
from applications.models import *
from parsley.decorators import parsleyfy


@parsleyfy
class categoryForms(forms.ModelForm):
    class Meta:
        model=categorys
        fields=["categorys_name"]

@parsleyfy
class sub_categoryForms(forms.ModelForm):
    class Meta:
        model = sub_categorys
        fields= ["sub_categorys_name","categorys_id"]

@parsleyfy
class stateForms(forms.ModelForm):
    class Meta:
        model = states
        fields=["states_name"]

@parsleyfy
class cityForms(forms.ModelForm):
    class Meta:
        model = citys
        fields = ["citys_name","states_id"]

@parsleyfy
class areaForms(forms.ModelForm):
    class Meta:
        model = areas
        fields = ["areas_name","citys_id"]

@parsleyfy
class docterForms(forms.ModelForm):
    docters_image=forms.FileField()
    class Meta:
        model = docters
        fields= ["docters_name","docters_image","docters_no","hospital_name","hospital_no","hospital_address",]

@parsleyfy
class productForms(forms.ModelForm):
    products_image=forms.FileField()
    class Meta:
        model = products
        fields = ["products_name","products_image","products_price","products_quantity","sub_categorys_id","products_description" ]

@parsleyfy
class galleryFroms(forms.ModelForm):
    images=forms.FileField()
    class Meta:
        model = gallerys
        fields = ['images','products_id']

class userFroms(forms.ModelForm):
    class Meta:
        model = users
        fields =['users_email','mobile_no','first_name','last_name',]

@parsleyfy
class RegisterFroms(forms.ModelForm):
    class Meta:
        model = users
        fields=['first_name','last_name','users_email','users_password','mobile_no','birth_of_date','users_address','areas_id'] 


class cus_proFroms(forms.ModelForm):
    class Meta:
        model = users
        fields=['first_name','last_name','users_email'] 