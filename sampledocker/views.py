from django.shortcuts import render
from . models import Number_user,user,Employee,Department,Book,Store
# Create your views here.
def index(request):
    # emp=Employee.objects.all().select_related('department_id')
    # print(emp)
    # for emp in emp:
    #     print(emp,)
    book = Book.objects.all()
    for book in book:
        print(book.stores.books)
   