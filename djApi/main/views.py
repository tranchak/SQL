from django.shortcuts import render
from .models import Auto, Brand, Detail


def home_page(request):
    auto = Auto.objects.filter()
    print(auto)
    context = {}
    return render(request, 'main/index.html', context)
