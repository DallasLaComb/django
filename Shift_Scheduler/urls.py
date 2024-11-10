from employee_app import views as employee_views
from manager_app import views as manager_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', employee_views.schedule, name='schedule'),
    path('admin/', admin.site.urls),
    path('second', manager_views.second, name='second'),
]
