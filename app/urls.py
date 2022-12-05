from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="templateview"),
    path("data/", views.data, name="datapage"),
    
    path("data/addproduct/", views.addproduct, name="addproduct"),
    path("data/addproduct/addrecord/", views.addrecord, name="addrecord"),
    
    path("data/delete/<int:pid>", views.delete, name="deleterecord"),
    
    path("data/update/<int:pid>", views.update, name="update"),
    path("data/update/update_product/<int:pid>", views.update_product, name="update_product"),

]
