from django.shortcuts import render
from .forms import MyForm
from .librerie.library import main,transform

# Create your views here.

def generatoreDiPosti(input):
    input, k =transform(input,3,7)
    if k==0:
        results=main(input)
    else:
        results = [item for row in input for item in row]
    return results,k



def posti(request):
    k=0
    results = None
    if request.method == 'POST':
        form = MyForm(request.POST)
        inputs=[]
        if form.is_valid():
            for i in range(21):
                inputs.append(form.cleaned_data[f'input{i+1}'].upper()) #creo l'array con i nomi in input per la prima configurazione dei posti
            results,k = generatoreDiPosti(inputs)
    else:
        form = MyForm()
    print(results)
    return render(request, 'posti/index.html', {'form': form, 'results': results, 'error':k})