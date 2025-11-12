from django.shortcuts import render, get_object_or_404
from .models import Animal
from django.core.paginator import Paginator

def animal_list(request):
    animals = Animal.objects.all()
    paginator = Paginator(animals, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'animals/animal_list.html', {'page_obj': page_obj})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animals/animal_detail.html', {'animal': animal})

def animal_of_the_day(request):
    animal = Animal.objects.filter(is_animal_of_the_day=True).first()
    return render(request, 'animals/animal_detail.html', {'animal': animal})

def next_animal_collection(request):
    animals = Animal.objects.filter(habitat='next')  
    paginator = Paginator(animals, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'animals/animal_list_next.html', {'page_obj': page_obj})