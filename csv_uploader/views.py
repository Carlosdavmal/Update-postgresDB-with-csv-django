import csv, io
from django.shortcuts import render
from .forms import RowFill
from .models import Row
from django.contrib import messages
import pandas as pd



def row(request):
    template = 'rowfill.html'

    if request.method =="POST":
        form = RowFill(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = RowFill()

    context = {
        'form':form,
    }

    return render(request, template, context)

def csv_form(request):
    if request.method =="POST":
        dataForm = ClassicForm(request.POST)
        if dataForm.is_valid():
            inform=dataForm.cleaned_data
            #Enviar a la bd
            return render(request,"addded.html")
    else:
        dataform=ClasicForm()

    return render(request,"csv_form.html",{"form":dataForm})
# Upload csv file
def csv_upload(request):
    
    template="csv_upload.html"
    prompt = {
    'order': 'order of csv should be first_name, last_name, email'
    }
    if request.method == "GET":
        return render(request, template, prompt)
    

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'this is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    #print(data_set)
    io_string = io.StringIO(data_set)
    next(io_string)
    #print(io_string)
    #banned=["0","1","2","3","4","5","6","7","8","9"]
    #

    #arreglar rise error, detener ejecución peron print
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):       
       
        if len(column[0]) > 20:
            messages.error(request, 'Maximo 20 caracteres')   
            break  
        if  column[0].isdigit():
            messages.error(request, 'Dataset no puede contener numeros')
            break   

        if len(column[1]) > 20:
            messages.error(request, 'Maximo 20 caracteres') 
            break       
        if  column[1].isdigit():
            messages.error(request, 'point no puede contener numeros')
            break

        if len(column[2]) > 20:
            messages.error(request, 'Maximo 20 caracteres')  
            break      
        if  column[2].isalpha():
            messages.error(request, 'client_id no puede contener letras')
            break

        if len(column[3]) > 45:
            messages.error(request, 'Maximo 45 caracteres') 
            break       
        if  column[3].isdigit():
            messages.error(request, 'client_name no puede contener numeros')
            break

        _, created = Row.objects.update_or_create(      
            dataset = column[0],
            point = column[1],
            client_id = column[2],
            client_name = column[3] 
        )
    context = {}
    return render(request, template, context)
        
        

    #for column in csv.reader(io_string, delimiter=',', quotechar='|'):
    #    _, created = Row.objects.update_or_create(      
    #        dataset = column[0],
    #        point = column[1],
    #        client_id = column[2],
    #        client_name = column[3]
    #   )
    
    #context = {}
    #return render(request, template, context)

def db_info_view(request):
    obj = Row.objects.get(id=1)
    context = {
        'dataset'
        'point'
        'client_id'
        'client_name'

    }

    return render(request, "info_view.html")