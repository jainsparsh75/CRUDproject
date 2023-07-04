from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # web crud urls
    path('', views.employee_form, name='employee_insert'),  # get and post req. for insert operation
    path('<int:id>/<str:val>', views.employee_form, name='employee_update'),  # get and post req. for update operation
    path('<int:id>/<str:val>', views.employee_form, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'),  # get req. to retrieve and display all records

    # path('employee-list/', views.employeeSerializerList, name='employee_list_serializer'),
    # path('employee-detail/<str:pk>/', views.employeeDetail, name='employee_detail'),

    # postman apis
    path('postman_form/',views.postman_form,name = 'postman_form'),
    path('postman_form/<int:id>',views.postman_form,name = 'postman_form_getid'),
    path('postman_form/delete/<int:id>',views.postman_form,name = 'postman_form_delete'),
    path('postman_form/update/<int:id>',views.postman_form,name = 'postman_form_update')
]
