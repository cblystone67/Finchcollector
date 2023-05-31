from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def all_finches_index(request):
  return render(request, 'all_finches/index.html', {'finches': finches})


finches = [
  {'species': 'Zebra Finch', 'diet': 'mainly seeds, grassses, greens', 'lifespan': '2-3 years', 'size': '10 cm', 'unique_characteristics': 'Elaborate male songs and complex courtship displays'},
  {'species': 'Gouldian Finch', 'diet': 'seeds, insects, fruits', 'lifespan': '4-6 years', 'size': '12 cm', 'unique_characteristics': 'strikingly colorful plumage with multiple variants'},
  {'species': 'Society Finch', 'diet': 'seeds, grains, greens', 'lifespan': '5-7 years', 'size': '12 cm', 'unique_characteristics': 'sociable and easy to keep in mixed aviary settings'},
]