from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .forms import BookForm
from .forms import LoginForm
from .forms import newLoginForm
from .models import Book
from .models import Login
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.contrib import messages


# Create your views here.
loginName = "ゲスト"

def index(request):
    n = name()
    params = {
        'form': LoginForm(),
        'data': Login.objects.all(),
        'name':n
    }
    if n == "ゲスト":
        return render(request, 'myapp/login.html', params)
    else:
        print(n)
        return render(request, 'myapp/index.html', params)
    

def name():
    global loginName
    if loginName == "ゲスト":
        return "ゲスト"
    else:
        return loginName

def signIn(name):
    if name == "ゲスト":
        return redirect(to='/login')
    else:
        print(name)
        return

def signOut(request):
    global loginName
    loginName = "ゲスト"
    return redirect(to='/')

def login(request):
    global loginName
    if request.method == 'POST':
        _id = request.POST.get('Loginid')
        p = request.POST.get('password')
        l = Login.objects.get(Loginid=_id,password=p)
        print(l,p)
        if l.password == p:
            loginName = _id
            return redirect(to='/')
        else:
            message = "パスワード、またはログインIDが異なります"
            return render(request, 'myapp/login.html', message)
    params = {
        'form': LoginForm(),
        'data': Login.objects.all()
    }
    return render(request, 'myapp/login.html', params)

def newlogin(request):
    params = {
        'form': newLoginForm(),
    }
    if request.method == 'POST':
        l = Login()
        #l.id = 1
        # l.Loginid = request.POST.get('Loginid')
        # l.password = request.POST.get('password')
        # l.mail = request.POST.get('mail')
        log = newLoginForm(request.POST,instance=l)
        if log.is_valid():
            log.save()
        else:
            print('ERROR FROM INVALID')
        return redirect(to='/')
    return render(request, 'myapp/login_new.html', params)

def lend(request):
    n = name()
    today = datetime.today()
    if request.method == 'POST':
        bookid = request.POST.get('hidden')
        print(bookid)
        isAv = request.POST.get('isAvailable')
        if isAv == "True":
            print("a")
            Book.objects.filter(bookid=bookid).update(isAvailable = False,deadline = today + relativedelta(months=1))
        else:
            print(isAv)
            Book.objects.filter(bookid=bookid).update(isAvailable = True,deadline = today + relativedelta(months=1))
        return redirect(to='/lend')

    q_word = request.GET.get('query')
    if q_word:
        data = Book.objects.filter(Q(title__icontains=q_word) | Q(author__icontains=q_word))
    else:
        data = Book.objects.all()
    params = {
        'data': data,
        'name':n
    }
    return render(request, 'myapp/lend.html', params)

def update(request):
    n = name()
    signIn(n)
    if request.method == 'POST':
        q = request.POST.get('hidden')
        i = int(q)
        data = Book.objects.filter(bookid=i)
        params = {
            'data': data,
            'form': BookForm(),
            'name':n
        }
        return render(request, 'myapp/update.html', params)
    return render(request, 'myapp/update.html', {})

def edit(request):
    today = datetime.today()
    bookid = request.POST.get('hidden')
    Book.objects.filter(bookid=bookid).update(
        updatedAt = timezone.now(),
        deadline =  today + relativedelta(months=1),
        isAvailable = True,
        title = request.POST.get('title'),
        author = request.POST.get('author'),
        producedby = request.POST.get('producedby'),
    )
    return redirect(to='/list')
    
def delete(request):
    n = name()
    signIn(n)
    if request.method == 'POST':
        q = request.POST.get('hidden')
        Book.objects.filter(bookid=q).delete()
        return redirect(to='/list')
    params = {
        'name':n
    }
    return render(request, 'myapp/index.html', params)

def register(request):
    n = name()
    signIn(n)
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
        'name':n
    }
    return render(request, 'myapp/register/register.html', params)

def list(request):
    n = name()
    signIn(n)
    q_word = request.GET.get('query')
    if q_word:
        data = Book.objects.filter(Q(title__icontains=q_word) | Q(author__icontains=q_word))
    else:
        data = Book.objects.all()
    params = {
        'data': data,
        'name':n
    }
    return render(request, 'myapp/list.html', params)

    

