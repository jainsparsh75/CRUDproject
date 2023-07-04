from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from rest_framework.decorators import api_view
from django.core.paginator import Paginator

from rest_framework.response import Response
from .serializers import EmployeeSerializer
from django.core.files.storage import FileSystemStorage
from .functions import insert_document, db_collection,check_document




def employee_list(request):
    print("inside list")
    # pagination
    employeeData = Employee.objects.all()
    paginator = Paginator(employeeData, 2)
    page_number = request.GET.get('page')
    employeeDataFinal = paginator.get_page(page_number)
    totalpages = employeeDataFinal.paginator.num_pages
    context = {'employee_list': employeeDataFinal,
               'pagesList': [n + 1 for n in range(totalpages)]}

    return render(request, "employee_register/employee_list.html", context)


# id =0 for insert(create)
# else for update
def employee_form(request, id=0, val='none'):
    print("value>>", val)
    print("id>>>>", id)
    if request.method == "GET" and val == 'none':
        form = EmployeeForm()
        print("inside get ")
        return render(request, "employee_register/employee_form.html", {'form': form})

    elif val == 'delete':
        print('insdie delete')
        employee = Employee.objects.get(pk=id)
        employee.delete()
        return redirect('/list')

    elif val == 'update':
        print('inside update')
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})

    else:
        print("val")
        print('inside post')
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')


# # serializers
# @api_view(['GET'])
# def employeeSerializerList(request):
#     employee = Employee.objects.all()
#     serializer = EmployeeSerializer(employee, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def employeeDetail(request,pk):
#     employee = Employee.objects.get(id =pk)
#     serializer = EmployeeSerializer(employee, many=False)
#     return Response(serializer.data)



@api_view(['POST'])
def upload_image(request):
    file_seria = EmployeeSerializer(data=request.data)
    if file_seria.is_valid():
        print('form is saved')
        file_seria.save()
        return Response({"successful": True})

# functions for postman apis
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def postman_form(request,id=-1):
    if request.method == "GET":
        response ={}
        if id ==-1:
            response = check_document({'flag': True})
        else:
            response = check_document({'id':id,'flag': True})

        if response['status'] == True:
            documents = response['document']
            result = []
            for document in documents:
                d = {}
                for key, value in document.items():
                    if key == "_id":
                        continue
                    else:
                        d[key] = value

                result.append(d)
            return Response({"successful": True, 'data': result})
        else:
            return Response({"successful": False})


    elif request.method == "POST":
        dict = {'id': int(request.data['id']),
                'fullname': request.data['fullname'],
                'emp_code': request.data['emp_code'],
                'mobile': int(request.data['mobile']),
                # 'image': request.data['image']
                'flag': True
                 }
        insert_document(dict)
        return Response({"successful": True})

    elif request.method =="DELETE":
        collection = db_collection()
        collection = collection['employee_register_employee']
        # for sofdelete
        updated = collection.update_one({'id': id}, {'$set': {'flag': False}})

        return Response({"successful": True})


    # for update when request.method =="PUT"
    elif request.method =="PUT":
        data = request.data
        collection = db_collection()
        collection = collection['employee_register_employee']
        updated = collection.update_one({'id':id},{'$set':{'mobile':int(data['mobile'])}})
        return Response({"successful": True})








