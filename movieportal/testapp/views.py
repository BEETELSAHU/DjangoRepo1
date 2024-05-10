from django.shortcuts import render
from .forms import MoviesForm
from .models import Movies

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def list_view(request):
    movie_list = Movies.objects.all()
    return render(request, 'list_movies.html', {'movie_list':movie_list})

def add_view(request):
    form = MoviesForm()
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)   
    return render(request, 'add_movie.html', {'form':form})
