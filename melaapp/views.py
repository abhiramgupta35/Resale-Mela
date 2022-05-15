from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect

from .filters import *
from .forms import *

# Create your views here.
from .models import *


def index(request):
    return render(request,'index.html')

def reg(request):
    return render(request, 'registration/reg.html')

def adhome(request):
    return render(request, 'adminpage/index.html')

def sehome(request):
    return render(request, 'sepage/index.html')

def cuhome(request):
    return render(request, 'customerpage/products_view.html')

def login(request):
    return render(request,'registration/login.html')

def userview(request):
    user = request.user
    if user.is_staff:
        return redirect('adhome')
    elif user.is_seller:
        return redirect('sehome')
    elif user.is_customer:
        return redirect('view_products')
    else:
        return redirect('index')

def signup(request):
    form = UserForm()
    r_form = RegForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        r_form = RegForm(request.POST, )
        if form.is_valid() and r_form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            s = r_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'CUSTOMER REGISTRATION SUCCESSFULL')
            return redirect('signup')
    return render(request, 'register.html', {'form': form, 'r_form': r_form})


def signup1(request):
    form = UserForm()
    r_form1 = SellForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        r_form1 = SellForm(request.POST, )
        if form.is_valid() and r_form1.is_valid():
            user = form.save(commit=False)
            user.is_seller = True
            user.save()
            s = r_form1.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'SELLER REGISTRATION SUCCESSFULL')
            return redirect('signup1')
    return render(request, 'register1.html', {'form': form, 'r_form1': r_form1})

def view_seller(request):
    dept = sellregister.objects.all()
    return render(request, 'adminpage/view_sellers.html', {'depts': dept})


def view_cus(request):
    dept = customeregister.objects.all()
    return render(request, 'adminpage/view_cust.html', {'depts': dept})


def add_category(request):
    a_form = CategoryForm()
    if request.method == 'POST':
        a_form = CategoryForm(request.POST, request.FILES)
        if a_form.is_valid():
            a_form.save()
            messages.info(request,'Added successfully')
            return redirect('add_category')
    return render(request,'sepage/add_category.html',{'a_form':a_form})



def view_category(request):
    d = category.objects.all()
    return render(request,'sepage/view_category.html',{'ds':d})

def delete_cat(request,id=None):
    data = category.objects.get(id=id)
    data.delete()
    return redirect('view_category')
def edit_cat(request,id=None):
    data = category.objects.get(id=id)
    a_form =CategoryForm(instance=data)
    if request.method=='POST':
        a_form = CategoryForm(request.POST,instance=data)
        if a_form.is_valid():
            a_form.save()
            return redirect('view_category')
    return render(request, 'sepage/edit_cat.html', {'a_form':a_form})

def add_product(request):
    u = sellregister.objects.get(user=request.user)
    p_form = ProductForm()
    if request.method == 'POST':
        p_form = ProductForm(request.POST,request.FILES)
        if p_form.is_valid():
            schedule = p_form.save(commit=False)
            schedule.seller = u
            schedule.save()
            messages.info(request, 'Product Added ')
            return redirect('add_product')
    return render(request, 'sepage/add_product.html', {'p_form': p_form})

def view_product(request):
    u = sellregister.objects.get(user=request.user)
    schedule = productt.objects.filter(seller=u)
    return render(request, 'sepage/view_product.html', {'schedules': schedule})

def delete_product(request,id=None):
    data = productt.objects.get(id=id)
    data.delete()
    return redirect('view_product')

def edit_product(request,id=None):
    data = productt.objects.get(id=id)
    p_form =ProductForm(instance=data)
    if request.method=='POST':
        p_form = ProductForm(request.POST, request.FILES,instance=data,)
        if p_form.is_valid():
            p_form.save()
            return redirect('view_product')
    return render(request, 'sepage/edit_product.html', {'p_form':p_form})



def view_products(request):
    product = productt.objects.all()
    serviceFilter = ServiceFilter(request.GET, queryset=product)
    product = serviceFilter.qs
    context = {
        'products': product,
        'serviceFilter': serviceFilter
    }
    return render(request, 'customerpage/products_view.html', context)


def view_categoryy(request):
    c = category.objects.all()
    return render(request, 'customerpage/products_view.html', {'categories': c})

def product_detail(request, id):
    product = productt.objects.filter(id=id)
    return render(request, 'customerpage/product_d.html', {'products': product})

def order_request(request, id):
    u = customeregister.objects.get(user=request.user)
    pro = productt.objects.get(id=id)
    if request.method == 'POST':
        acc = request.POST.get('product')
        card_number = request.POST.get('card_number')
        cvv = request.POST.get('cvv')
        ob = CustomerRequest()
        ob.pro = pro
        ob.card_number = card_number
        ob.cvv = cvv
        ob.payment_status = 1
        ob.customer = u
        req = CustomerRequest.objects.filter(customer=u, pro=pro)
        if req.exists():
            messages.info(request, 'You Already Applied for this Product ')
        else:
            ob.save()
            messages.info(request, 'Request send ')
            return redirect('cus_request_status')

    return render(request, 'customerpage/order_request.html', {'key': pro})

def cus_request_status(request):
    u = customeregister.objects.get(user=request.user)
    order = CustomerRequest.objects.filter(customer=u)
    return render(request, 'customerpage/order_status.html', {'orders': order})

def cus_request_order(request):
    u = sellregister.objects.get(user=request.user)
    product = CustomerRequest.objects.filter(pro__seller=u)
    return render(request, 'sepage/view_cusorders.html', {'products': product})

def approve_cus(request, id):
    req = CustomerRequest.objects.get(id=id)
    req.order_status = 1
    req.save()
    messages.info(request, 'Approved ')
    return redirect('cus_request_order')


def reject_cus(request, id):
    req = CustomerRequest.objects.get(id=id)
    req.order_status = 2
    req.save()
    messages.info(request, 'Rejected ')
    return redirect('cus_request_order')

def s_feedback(request):
    u = customeregister.objects.get(user=request.user)
    w_form = SfeedbackForm()
    if request.method == 'POST':
        w_form = SfeedbackForm(request.POST)
        if w_form.is_valid():
            pro = w_form.save(commit=False)
            pro.customer = u
            pro.save()
            messages.info(request, 'Feedback send successfully')
            return redirect('s_feedback')
    return render(request, 'customerpage/feedback.html', {'w_form': w_form})

def view_cfeedback(request):
    product = Cfeedback.objects.all()
    return render(request, 'adminpage/view_feedback.html', {'products': product})



