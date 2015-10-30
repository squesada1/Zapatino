from django.shortcuts import render 

def formulario_index(request): 
    return render(request,'zapatino_templates/index.html') 
def formulario_empresa(request): 
    return render(request,'zapatino_templates/empresa.html')

