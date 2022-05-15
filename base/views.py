from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from matplotlib.style import context
from .models import Address, CheckOut, Employee, MobilePhone, User, Product, Book, Clothes, Category, OrderProduct, Cart, Function, Comment
from .form import UserForm, MyUserCreationForm, MobilePhoneForm, BookForm, ClothesForm, AddressForm, CommentForm



# Create your views here.

def Home(request):
    if request.user.is_authenticated:
        if request.user.functionality_of_user.name == 'Employee':
            request.user = Employee.objects.get(id=request.user.id)
            
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user__id = request.user.id)
        except:
            cart = {}
    else:
        cart = {}
    categorys = Category.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(Q(name__icontains=q) | Q(category__name__icontains = q))
    products = sorted(products, key=lambda x: -(x.category.name == 'Book' or x.category.name == 'Clothes'))
    context = {'products':products, 'categorys':categorys, 'cart': cart}
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

# ----------------------------------------------------------------------------------#
def Logout(request):
    logout(request)
    return redirect ('home')

# ----------------------------------------------------------------------------------#
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

# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def Manager(request):

    page = ''
    try:
        user = Employee.objects.get(id = request.user.id)
        if user.position == 'Product manager':
            page = 'manage-product'
        elif user.position == 'Order manager':
            page = 'manage-order'
    except:
        page = 'not permission'

    if request.user.is_staff:
        page = 'Admin'      

    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categorys = Category.objects.all()
    products = Product.objects.filter(Q(name__icontains = q) | Q(category__name__icontains = q))
    checkouts = CheckOut.objects.filter(Q(address_delivery__receiver__icontains = q))
    checkouts = sorted(checkouts, key = lambda x: -(x.status_order == 'in warehouse'or  x.status_order == 'delivering'))

    if request.method == 'POST' and 'submit_category' in request.POST:
        selected = request.POST.get('category', None)
        return redirect('create-product', selected)
    if request.method =='POST' and 'update_checkout' in request.POST:
        for checkout in checkouts:
            checkout.status_order = request.POST.get(f"status_order_{checkout.id}")
            checkout.save()
        messages.error(request,'Udpate status orders successful')
    context = {'categorys' : categorys, 'products': products, 'cart': {}, 'checkouts':checkouts, 'page': page}
    return render(request, 'base/manage.html', context)

# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def DeleteProduct(request, pk):
    if request.user.functionality_of_user.name == 'Admin' or request.user.functionality_of_user.name == 'Employee':
        try:
            product = Product.objects.get(id= pk)
        except:
            messages.error(request, 'This product is not exist')
            return redirect('manage')
        try:
            product.delete()
            messages.success(request, 'Delete product successful')
            return redirect('manage')
        except:
            messages.error(request,'You can\'t delete this product')

        return redirect('manage')
    else:
        messages.error(request, 'You can\'t delete products')
        return redirect('home')
# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def createProduct(request, CategoryId):
    if request.user.functionality_of_user.name == 'Admin' or request.user.functionality_of_user.name == 'Employee': 
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
    else:
        messages.error(request, 'you can\'t create product')
        return redirect('home')
# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def updateProduct(request, CategoryId, pk):
    if request.user.functionality_of_user.name == 'Admin' or request.user.functionality_of_user.name == 'Employee': 
        try:
            category = Category.objects.get(id=CategoryId)
            product = Product.objects.get(id = pk)
        except:
            messages.error(request,'Product not exist!')
            return redirect('manage')
        if category.name == 'Book':
            form = BookForm(instance=product)
        elif category.name == 'Mobile Phone':
            form = MobilePhoneForm(instance=product)
        elif category.name =='Clothes':
            form = ClothesForm(instance=product)

        if request.method == 'POST':
            if category.name == 'Book':
                form = BookForm(request.POST, request.FILES, instance=product)
            elif category.name == 'Mobile Phone':
                form = MobilePhoneForm(request.POST, request.FILES, instance=product)
            elif category.name == 'Clothes':
                form = ClothesForm(request.POST,request.FILES, instance=product)
            
            if form.is_valid():
                product = form.save(commit=False)
                product.category = category
                product.save()
                messages.success(request, 'Update product successful')
                return redirect('manage-product')
            else:
                messages.error(request, 'Some fields not vaild')
        context = {'category': category.name, 'form': form, 'cart': {}}
        return render(request, 'base/update-product.html', context)
    else:
        messages.error(request, 'you can\'t update product')
        return redirect('home')
        
# ----------------------------------------------------------------------------------#
def orderProduct(request, CategoryId, pk):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user__id = request.user.id)
        except:
            cart = {}
    else:
        cart = {}
    product = None
    form = None
    category = Category.objects.get(id= CategoryId)
    if category.name == 'Book':
        try:
            product = Book.objects.get(id=pk)
            form = BookForm(instance=product)
        except:
            messages.error(request, 'This product is not exist!')
    elif category.name == 'Mobile Phone':
        try:
            product = MobilePhone.objects.get(id=pk)
            form = MobilePhoneForm(instance=product)
        except:
            messages.error(request, 'This product is not exist!')
    elif category.name =='Clothes':
        try:
            product = Clothes.objects.get(id=pk)
            form = ClothesForm(instance=product)
        except:
            messages.error(request, 'This product is not exist!')
    try:
        comments = Comment.objects.filter(product = product)
    except:
        comments = None
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
        
    context = {'product':product, 'category':category.name, "form":form, 'cart': cart, "comments": comments}
    
    return render(request, 'base/order-product.html', context)

# ----------------------------------------------------------------------------------#
def buyNow(request, pk):
    try:
        product = Product.objects.get(id=pk)
        orderProduct = OrderProduct.objects.create(
            user = request.user,
            product = product,
            quantity = 1,
        )
        
        cart = Cart.objects.get(user_id = request.user.id)
        orderOfUsers = cart.order.all()

        flag = False
        for orderOfUser in orderOfUsers:
            if orderOfUser.product.id == product.id:
                orderOfUser.quantity = orderOfUser.quantity + 1
                orderOfUser.save()
                flag = True

        if flag == False:
            cart.order.add(orderProduct)
    except:
        messages.error(request, 'This product in not exist')
        return redirect('home')
    messages.success(request, 'Added product to your cart')
    return redirect('home')

# ----------------------------------------------------------------------------------#
def manageOrder(request):

    context = {}
    return render(request, 'base/manage-order.html', context)

# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def cart(request):
    try:
        cart = Cart.objects.get(user__id = request.user.id)
    except:
        cart = {}
    address = Address.objects.filter(Q(user__id = request.user.id) & Q(boolean =True))
    if request.method == 'POST':
        for order in cart.order.all():
            id_quantity = 'quantity-product-cart-' + str(order.id) 
            order.quantity = request.POST.get(id_quantity)
            order.save()

        if address:
            checkbox_order_id = request.POST.getlist('checkbox_products[]') 
            if checkbox_order_id:
                check_out = CheckOut.objects.create(
                    user = request.user,
                    address_delivery = address[0]
                )

                for id_order_selected in checkbox_order_id:
                    try:
                        order_selected = cart.order.get(id=int(id_order_selected))
                        check_out.order_Items.add(order_selected)
                        cart.order.remove(order_selected)
                        messages.success(request, 'order successful')
                    except:
                        messages.error(request, 'Cant add order to check out')
            else:
                messages.error(request, 'You have to selected some order to buy!')
        else:
            messages.error(request, 'Please select an address for delivery')

    context = {'cart': cart, 'address' : address}

    return render(request, 'base/cart.html', context)

# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def deleteOrder(request, orderId):

    try:
        cart = Cart.objects.get(user = request.user)
        order = cart.order.get(id = orderId)
        cart.order.remove(order)
        messages.success(request, 'Delete order successful'); 
    except:
        messages.error(request, 'You can\'t delete this order');    
    return redirect('cart') 

# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def chooseAddressDelivery(request):
    try:
        cart = Cart.objects.get(user__id = request.user.id) 
    except:
        cart = {}
    list_address = Address.objects.filter(Q(user = request.user))
    list_address = sorted(list_address, key=lambda x: -(x.boolean))
    if request.method == 'POST':
        for address in list_address:
            if  str(address.id) in request.POST:
                address.boolean = True
            else:
                address.boolean = False
            address.save()

        return redirect('cart')

    context = {'cart' : cart, 'list_address': list_address,}
    return render(request, 'base/choose-address-delivery.html', context)

# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def updateAddressDelivery(request, pk):
    page = 'update'
    address = Address.objects.get(id=pk)
    form = AddressForm(instance = address)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance = address)
        try:
            form.save()
            messages.success(request, 'Update address for delivery successful') 
            return redirect('choose-address-delivery')
        except:
            messages.error(request, 'Have an error')
    context = {'form': form, 'page': page}
    return render(request, 'base/update-add-address-delivery.html', context)

# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def addAdressDelivery(request):
    page = 'add'
    form = AddressForm()
    
    if request.method =='POST':

        form = AddressForm(request.POST)

        try:
            address =  form.save(commit=False)
            address.user = request.user
            address.boolean = False
            address.save()
            messages.success(request, 'Add address for delivery successful') 
            return redirect('choose-address-delivery')
        except:
            messages.error(request, 'have an error') 

    context = {'form': form, 'page': page}
    return render(request, 'base/update-add-address-delivery.html', context)

# ----------------------------------------------------------------------------------#
@login_required(login_url='login')
def deleteAddressDelivery(request, pk):
    address = Address.objects.get(id=pk)
    
    try:
        address.delete()
        messages.success(request, 'Delete address successful')
        return redirect('choose-address-delivery')
    except:
        messages.error(request, 'Sorry have an error') 

    context = {}
    return render(request, 'base/choose-address-delivery.html', context)


@login_required(login_url='login')
def viewOrder(request):
    checkouts = CheckOut.objects.filter(Q(user = request.user) & (Q(status_order = 'in warehouse') | Q(status_order = 'delivering')))
    checkouts = sorted(checkouts, key=lambda x: -(x.status_order =='in warehouse'))
    try:
        cart = Cart.objects.get(user = request.user)
    except:
        cart = {}
    ordereds = CheckOut.objects.filter(Q(user = request.user) and Q(status_order = 'completed'))

    context = {'checkouts' : checkouts, 'cart': cart, 'ordereds': ordereds}
    return render(request, 'base/view-order.html', context)


def write_comment(request, categoryID, productID):
    permission = "no"
    try:
        cart = Cart.objects.get(user=request.user)
    except:
        cart = {}

    category = Category.objects.get(id=categoryID)
    if category.name == "Mobile Phone":
        try:
            product = MobilePhone.objects.get(id=productID)
        except:
            product = None
            messages.error(request, 'This product is not exist!')
    elif category.name == "Clothes":
        try:
            product = Clothes.objects.get(id=productID)
        except:
            product = None
            messages.error(request, 'This product is not exist!')
    elif category.name == "Book":
        try:
            product = Book.objects.get(id=productID)
        except:
            product = None
            messages.error(request, 'This product is not exist!')
    checkouts = CheckOut.objects.filter(Q(user = request.user) & Q(status_order = 'completed'))
    try:
        for checkout in checkouts:
            orders = checkout.order_Items.all()
            for order in orders:
                if product.id == order.product.id:
                    permission = 'yes'
                    break
            if permission == 'yes':
                break
    except:
        pass
    form = CommentForm()
    if request.method == 'POST':
        try:
            form = CommentForm(request.POST)
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            messages.success(request, 'Comment successful')
            return redirect('view-order')
        except:
            messages.error(request, 'Error') 

    context = {'product': product, 'form': form, 'permission' : permission, 'cart': cart}
    return render(request, 'base/write-comment.html', context)
