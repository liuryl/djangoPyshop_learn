from django.urls import path
from . import views



# /poducts
# /product/1/detail
urlpatterns=[
    #添加新页
    path('',views.index),
    # 添加新页new
    path('new',views.new)
]