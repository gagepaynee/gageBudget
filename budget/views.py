from django.shortcuts import render
from .models import Expense

# Create your views here.
def home_page(request):
    expenses = Expense.objects.all()
    return render(request, 'budget/index.html', {'expenses': expenses})