import csv, io
from django.shortcuts import render
from .forms import RowFill
from .models import Row
from django.contrib import messages



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
    print(data_set)
    io_string = io.StringIO(data_set)
    next(io_string)
    print(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Row.objects.update_or_create(      
            dataset = column[0],
            point = column[1],
            client_id = column[2],
            client_name = column[3]
        )
    
    context = {}
    return render(request, template, context)