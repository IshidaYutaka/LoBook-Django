from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .forms import BookForm
from .models import Book
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Q
 

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html', {})

def login(request):
    return render(request, 'myapp/login.html', {})

def lend(request):
    q_word = request.GET.get('query')
    if q_word:
        data = Book.objects.filter(Q(title__icontains=q_word) | Q(author__icontains=q_word))
    else:
        data = Book.objects.all()
    params = {
        'data': data
    }
    return render(request, 'myapp/lend.html', params)

def update(request):
    if request.method == 'POST':
        q = request.POST.get('update')
        data = Book.objects.filter(bookid=q)
        params = {
        'data': data
        }
        return render(request, 'myapp/update.html', params)
    return render(request, 'myapp/update.html', {})

def delete(request):
    if request.method == 'POST':
        q = request.POST.get('hidden')
        i = int(q)
        Book.objects.filter(bookid=q).delete()
        return redirect(to='/list')
    return render(request, 'myapp/index.html', {})

def register(request):
    if request.method == 'POST':
        b = Book()
        b.bookid = len(Book.objects.order_by('-bookid'))+1
        b.createdAt = timezone.now()
        b.updatedAt = timezone.now()
        b.deadline = datetime.today() + relativedelta(months=1)
        b.isAvailable = True
        b.producedby = "不明"
        # b.purchaseDate = timezone.now()
        book = BookForm(request.POST,instance=b)
        if book.is_valid():
            book.save()
        else:
            print('ERROR FROM INVALID')
        return redirect(to='/')
    params = {
        'form': BookForm(),
    }
    return render(request, 'myapp/register/register.html', params)

def list(request):
    q_word = request.GET.get('query')
    if q_word:
        data = Book.objects.filter(Q(title__icontains=q_word) | Q(author__icontains=q_word))
    else:
        data = Book.objects.all()
    params = {
        'data': data
    }
    return render(request, 'myapp/list.html', params)

    

