from django.shortcuts import render, redirect
from .models import Film

def add_film(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        review = request.POST.get('review')

        # Сохраняем данные в базу
        Film.objects.create(title=title, description=description, review=review)
        return redirect('film_list')

    return render(request, 'films/add_film.html')

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})