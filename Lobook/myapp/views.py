from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .forms import BookForm
from .models import Book
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html', {})

def register(request):
    if request.method == 'POST':
        b = Book()
        b.bookid = len(Book.objects.order_by('-bookid'))+1
        b.createdAt = timezone.now()
        b.updatedAt = timezone.now()
        b.deadline = datetime.today()
        b.isAvailable = False
        b.producedby = "集英社"
        # b.purchaseDate = timezone.now()
        book = BookForm(request.POST,instance=b)
        if book.is_valid():
            book
            book.save()
        else:
            print('ERROR FROM INVALID')
        return redirect(to='/')
    params = {
        'form': BookForm(),
    }
    return render(request, 'myapp/register/register.html', params)

def list(request):
    data = Book.objects.all()
    params = {
        'data': data
    }
    return render(request, 'myapp/list.html', params)
