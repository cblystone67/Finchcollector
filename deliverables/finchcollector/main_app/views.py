from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Finch, Toy
from .forms import FeedingForm

# Create your views here.

def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

@login_required
def all_finches_index(request):
  finches = Finch.objects.filter(user=request.user)
  return render(request, 'all_finches/index.html', {'finches': finches})

@login_required
def all_finches_details(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.toys.all().values_list('id')
  toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'all_finches/details.html', {'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have})

@login_required
def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('details', finch_id=finch_id)

@login_required
def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('details', finch_id=finch_id)

@login_required
def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('details', finch_id=finch_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form, 'error': error_message}) 


class FinchCreate(LoginRequiredMixin, CreateView):
  model = Finch
  fields = ['species', 'diet', 'lifespan', 'size', 'unique_characteristics']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  
class FinchUpdate(LoginRequiredMixin, UpdateView):
  model = Finch
  fields = ['diet', 'lifespan', 'size', 'unique_characteristics']
  
  
class FinchDelete(LoginRequiredMixin, DeleteView):
  model = Finch
  success_url = '/all_finches/'


class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = ['name', 'color']

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'