from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('add_course',views.add_course,name='add_course'),
    path('details/<course_id>',views.details,name='details'),
    path('orders/<course_id>',views.buy,name='orders'),
    path('my_order',views.orders,name='my_orders'),
]