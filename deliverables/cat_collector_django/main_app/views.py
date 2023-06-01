from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Cat

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', {'cat': cat})

class CatCreate(CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']
  # success_url = '/cats/'
  # Can do it this way, but not preferred way.
  
class CatUpdate(UpdateView):
  model = Cat
  fields = ['description', 'age']
  
  
class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'
  # When deleting you use this method of redirecting because there wont be a model left it will be empty.