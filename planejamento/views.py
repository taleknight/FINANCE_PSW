from django.shortcuts import render
from perfil.models import Categoria
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    #novo_valor = json.load(request)['novo_valor']
    #categoria = Categoria.objects.get(id=id)
    #categoria.valor_planejamento = novo_valor
    #categoria.save()

    return JsonResponse({'valor': f'Recebi o valor {id}'})