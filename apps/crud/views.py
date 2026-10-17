from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza
from .forms import PizzaForm

@login_required
def index(request):
    pizzas = Pizza.objects.all()
    return render(request, "index.html", {
        'pizzas': pizzas,
    })


@login_required
def nova_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)

        if form.is_valid():
            pizza = form.save()
            print(f'Pizza salva com sucesso: {pizza.id}')
            return redirect('nova_pizza_sucesso')
        else:
            print('ERROS DO FORMULÁRIO:', form.errors)
    else:
        form = PizzaForm()

    return render(request, 'nova-pizza.html', {
        'form': form,
        'categorias': Pizza.CATEGORIAS,
    })

@login_required
def alterar_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)

    else:
        form = PizzaForm(instance=pizza)

    return render(request, 'alterar-pizza.html', {
        'form': form,
        'pizza': pizza,
        'categorias': Pizza.CATEGORIAS,
    })

  

@login_required
def excluir_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    pizza.delete()
    return redirect('index')

@login_required
def buscar_pizza(request):
    query = request.GET.get('buscar', '').strip()

    pizzas = Pizza.objects.filter(nome__icontains=query)

    return render(request, 'index.html', {
        'pizzas': pizzas,
        'query': query,
    })
    
@login_required
def nova_pizza_sucesso(request):
    return render(request, 'nova-pizza-sucesso.html')