from django.shortcuts import render, redirect
from app.models import slider, banner_area, main_cat, product, cat,color,brand,coupen_code
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Max, Min


from app.models import product
from cart.cart import Cart



# Create your views here.

def base(request):
    sliders = slider.objects.all().order_by('-id')[0:3]
    baners = banner_area.objects.all().order_by('-id')[0:3]
    main_catt = main_cat.objects.all()
    product_d = product.objects.filter(section__name="Top deal of the Day")
    context = {
        'sliders': sliders,
        'baners': baners,
        'main_catt': main_catt,
        'product_d': product_d
    }

    return render(request, 'index.html', context)


def product_detail(request, slug):
    products = product.objects.filter(slug=slug)

    if products.exists():
        products = product.objects.get(slug=slug)
    else:
        return redirect('404')

    context = {
        "products": products
    }

    return render(request, 'product/product-details.html', context)


def error404(request):
    return render(request, "error/404.html")


def my_account(request):
    return render(request, 'account/my.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "user exist")
            return redirect('login')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email exist')
            return redirect('login')

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        return redirect('login')


def log(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            # Display an error message for invalid login credentials
            messages.error(request, "Invalid username or password.")
            return redirect('login')


@login_required(login_url='/accounts/login/')
def profile(requset):
    return render(requset, 'profile/profile.html')


@login_required(login_url='/accounts/login/')
def profile_update(requset):
    if requset.method == "POST":
        username = requset.POST.get('username')
        first_name = requset.POST.get('first_name')
        last_name = requset.POST.get('last_name')
        email = requset.POST.get('email')
        password = requset.POST.get('password')
        user_id = requset.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != '':
            user.set_password(password)
            user.save()
            messages.success(requset, 'update')

            return redirect('base')


def about(requset):
    return render(requset, 'about.html')


def contact(requset):
    return render(requset, 'contact.html')


def product_main(requset):
    cata = cat.objects.all()
    products = product.objects.all()
    colord = color.objects.all()
    brands = brand.objects.all()
    print('this',colord)

    min_price = product.objects.all().aggregate(Min('price'))
    max_price = product.objects.all().aggregate(Max('price'))
    colorid = requset.GET.get('colorID')
    print('this',min_price,max_price)

    FilterPrice = requset.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        products = product.objects.filter(price__lte=Int_FilterPrice)
    elif colorid:
        products = product.objects.filter(color=colorid)

    else:
        products = product.objects.all()





    context = {

        'cata': cata,
        'products': products,
        'min_price' : min_price,
        'max_price' : max_price,
        'FilterPrice': FilterPrice,
        'colord': colord,
        "brands" : brands


    }

    return render(requset, 'product/Product_main.html', context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    brandss = request.GET.getlist('brands[]')
    print('this',brandss)

    allProducts = product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(categories__id__in=categories).distinct()

    if len(brandss) > 0:
        allProducts = allProducts.filter(brand__id__in=brandss).distinct()


    t = render_to_string('ajax/product.html', {'product': allProducts})

    return JsonResponse({'data': t})













@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    products = product.objects.get(id=id)
    cart.add(product=products)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    products = product.objects.get(id=id)
    cart.remove(products)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    products = product.objects.get(id=id)
    cart.add(product=products)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    products = product.objects.get(id=id)
    cart.decrement(product=products)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    cart = request.session.get('cart')
    packing_cost = sum(i['packing_cost'] for i in cart.values() if i)
    tax = sum(i['tax'] for i in cart.values() if i)
    print(packing_cost,tax)
    coupon =  None
    valid = None
    not_valid =None

    if request.method == 'GET':
        coupon_code = request.GET.get('coupon_code')
        if coupon_code:
            try:
                coupon = coupen_code.objects.get(code = coupon_code)
                valid = 'Are applicabel on product'
            except:
                 not_valid= 'Not vaild coupon_code'


    context = {
        'packing_cost': packing_cost,
        'tax' : tax,
        'coupon' : coupon,
        'valid' : valid,
        'not_valid' : not_valid
    }
    return render(request, 'cart/cart.html',context)
