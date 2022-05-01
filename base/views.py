from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from matplotlib.style import context
from .models import Address, Employee, MobilePhone, User, Product, Book, Clothes, Category, OrderProduct, Cart, Function
from .form import UserForm, MyUserCreationForm, MobilePhoneForm, BookForm, ClothesForm, AddressForm



# Create your views here.

def Home(request):
    # if request.user.is_staff:
    #     print('admin')
    # else:
    #     print('Normal user')
    if request.user.is_authenticated:
        if request.user.functionality_of_user.name == 'Employee':
            request.user = Employee.objects.get(id=request.user.id)
            
    if request.user.is_authenticated:
        cart = Cart.objects.get(user__id = request.user.id)
    else:
        cart = {}
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    books = {}
    phones = {}
    clothes = {}
    topics = Category.objects.all()
    if(q=='Book'):
        books = Book.objects.all()
    elif(q=='Clothes'):
        clothes = Clothes.objects.all()
    elif(q=='Mobile Phone'):
        phones = MobilePhone.objects.all()
    else:
        books = Book.objects.filter(name__icontains = q)
        phones = MobilePhone.objects.filter(name__icontains = q)
        clothes = Clothes.objects.filter(name__icontains = q)
    context = {'books': books, 'phones':phones, 'clothes':clothes, 'topics':topics, 'cart': cart}
    return render(request, 'base/home.html', context)

def Login(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Password is not correct')

        except:
            messages.error(request, 'Email does not exist')

    context = {'page': page, 'cart': {}}
    return render(request, 'base/login-register.html', context)

def Logout(request):
    logout(request)
    return redirect ('home')

def registerPage(request):
    form = MyUserCreationForm()
    funtionality = Function.objects.get(name = 'Customer')
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        try:
            emailExist = User.objects.get(email= request.POST['email'].lower())
            messages.error(request, 'Email already exists, try another')
        except:
            pass

        try:
            userName = User.objects.get(username = request.POST['username'].lower())
            messages.error(request, 'Username already exists, try another')
        except:
            pass

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.functionality_of_user = funtionality
            user.save()
            login(request, user)
            Cart.objects.create(
                user = request.user
            )
            messages.success(request,'Register successful')
            return redirect('home')
        else:
            messages.error(request, 'Name or Username must be not contain space, special characters. Password and password confirm must be same and more than 8 character')

    return render(request, 'base/login-register.html', {'form': form, 'cart': {}})

@login_required(login_url='login')
def ManagerProduct(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    category = Category.objects.all()
    products = Product.objects.filter(Q(name__icontains = q) | Q(category__name__icontains = q))
    if request.method == 'POST':
        selected = request.POST.get('category', None)
        return redirect('create-product', selected)
    context = {'category' : category, 'products': products, 'cart': {}}
    return render(request, 'base/manage-product.html', context)

# def chooseProduct(request):

@login_required(login_url='login')
def DeleteProduct(request, pk):
    
    product = Product.objects.get(id= pk)
    try:
        product.delete()
        messages.success(request, 'Delete product successful')
        return redirect('manage-product')
    except:
        messages.error(request,'You can\'t delete this product')

    return redirect('manage-product')

@login_required(login_url='login')
def createProduct(request, CategoryId):
    category = Category.objects.get(id=CategoryId)
    if category.name == 'Mobile Phone':
        form  = MobilePhoneForm()
    elif category.name == 'Book':
        form = BookForm()
    elif category.name == 'Clothes':
        form = ClothesForm()

    if request.method =='POST':
        if category.name == 'Book':
            form = BookForm(request.POST, request.FILES)
        elif category.name == 'Mobile Phone':
            form = MobilePhoneForm(request.POST, request.FILES)
        elif category.name =='Clothes':
            form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = category
            form.save()
            messages.success(request, 'Create product successful')
            return redirect('manage-product')
        else:
            messages.error(request, 'Some fields not vaild')
    context = {'form' : form, 'product': category.name, 'cart': {}}
    return render(request, 'base/add-product.html', context)

@login_required(login_url='login')
def updateProduct(request, CategoryId, pk):
    category = Category.objects.get(id=CategoryId)
    if category.name == 'Book':
        book = Book.objects.get(id=pk)
        form = BookForm(instance=book)
    elif category.name == 'Mobile Phone':
        phone = MobilePhone.objects.get(id=pk)
        form = MobilePhoneForm(instance=phone)
    elif category.name =='Clothes':
        clothes = Clothes.objects.get(id=pk)
        form = ClothesForm(instance=clothes)

    if request.method == 'POST':
        if category.name == 'Book':
            form = BookForm(request.POST, request.FILES, instance=book)
        elif category.name == 'Mobile Phone':
            form = MobilePhoneForm(request.POST, request.FILES, instance=phone)
        elif category.name == 'Clothes':
            form = ClothesForm(request.POST,request.FILES, instance=clothes)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Update product successful')
            return redirect('manage-product')
        else:
            messages.error(request, 'Some fields not vaild')
    context = {'category': category.name, 'form': form, 'cart': {}}
    return render(request, 'base/update-product.html', context)

def orderProduct(request, CategoryId, pk):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user__id = request.user.id)
    else:
        cart = {}
    category = Category.objects.get(id= CategoryId)
    if category.name == 'Book':
        product = Book.objects.get(id=pk)
        form = BookForm(instance=product)
    elif category.name == 'Mobile Phone':
        product = MobilePhone.objects.get(id=pk)
        form = MobilePhoneForm(instance=product)
    elif category.name =='Clothes':
        product = Clothes.objects.get(id=pk)
        form = ClothesForm(instance=product)

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if not request.user.is_authenticated:
            messages.error(request, 'You have to login first to order')
            return redirect('login')
        
        else:
            orderProduct = OrderProduct.objects.create(
                user = request.user,
                product = product,
                quantity = quantity,
            )
            
            cart = Cart.objects.get(user_id = request.user.id)
            orderOfUsers = cart.order.all()

            flag = False
            for orderOfUser in orderOfUsers:
                if orderOfUser.product.id == product.id:
                    orderOfUser.quantity = orderOfUser.quantity + int(quantity)
                    orderOfUser.save()
                    flag = True

            if flag == False:
                cart.order.add(orderProduct)

            messages.success(request, 'Added product to your cart')
        
    context = {'product':product, 'category':category.name, "form":form, 'cart': cart}
    return render(request, 'base/order-product.html', context)

def manageOrder(request):

    context = {}
    return render(request, 'base/manage-order.html', context)

@login_required(login_url='login')
def cart(request):
    
    cart = Cart.objects.get(user__id = request.user.id)

    list_address = Address.objects.filter(Q(user__id = request.user.id))
    
    for address in list_address:
        print(address.boolean)


    if request.method == 'POST':
        for order in cart.order.all():
            id_quantity = 'quantity-product-cart-' + str(order.id) 
            order.quantity = request.POST.get(id_quantity)
            order.save()
        checkbox_order_id = request.POST.getlist('checkbox_products[]')
        
    context = {'cart': cart}

    return render(request, 'base/cart.html', context)

@login_required(login_url='login')
def deleteOrder(request, cartId, orderId):

    try:
        cart = Cart.objects.get(id = cartId)
        order = cart.order.get(id = orderId)
        cart.order.remove(order)
    except:
        messages.error(request, 'You can\'t delete this order');    
    return redirect('cart') 

@login_required(login_url='login')
def updateInforDelivery(request):
    cart = Cart.objects.get(user__id = request.user.id) 
    
    form = AddressForm()

    list_address = Address.objects.filter(Q(user = request.user))
    
    context = {'form': form, 'cart' : cart, 'list_address': list_address}
    return render(request, 'base/update-infor-delivery.html', context)