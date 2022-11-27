from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.http import JsonResponse
from .models import Product,Profile,BiddingItem
from django.contrib.auth.models import User
from django.db import IntegrityError
from datetime import datetime


def init():
    try:
        User.objects.create_user("boredapeyachtclub", "boredapeyachtclub@gmail.com", "yo")
        User.objects.create_superuser("yaleye", "yaleye@gmail.com", "yo")
    except:
        user = User.objects.filter(username="boredapeyachtclub").all()[0]
    boredApe = Product(category="NFT", title="boredApe", price="500000", description="One unique bored Ape", seller=user, currentHolder=user, image=os.path.join("static/boredape.png"))
    boredApe.save()

    cybertruck = Product(category="Vehicle", title="cybertruck", price="5000", description="new truck, fully powered by Electricity", seller=user, currentHolder=user, image=os.path.join("static/cybertruck.png"))
    cybertruck.save()

    lenses = Product(category="Lenses", title="rf24-105", price="1299", description="RF 24-105 F4 lenses", seller=user, currentHolder=user, image=os.path.join("static/lense.png"))
    lenses.save()

    macbook = Product(category="Computer", title="macbook", price="500", description="one unit of macbook with m2 chip", seller=user, currentHolder=user, image=os.path.join("static/macbook.png"))
    macbook.save()

    mars = Product(category="Planet", title="Mars", price="50000000", description="Planet Mars", seller=user, currentHolder=user, image=os.path.join("static/mar.png"))
    mars.save()

    metaverse = Product(category="MetaVerse", title="Metaverse", price="5", description="located at IP 222:222:222:222",seller=user, currentHolder=user, image=os.path.join("static/metaverse.png"))
    metaverse.save()

    canon = Product(category="Camera", title="R5", price="3899", description="8K Raw, 45MP, 4k 120", seller=user, currentHolder=user, image=os.path.join("static/r5.png"))
    canon.save()

    razerBape = Product(category="Collab", title="razer-Bape-Collab", price="500", description="Razer Collab with bape", seller=user, currentHolder=user, image=os.path.join("static/razer.png"))
    razerBape.save()

    scotland = Product(category="Land", title="Scotland", price="5000000", description="Whole scotland is on sale", seller=user, currentHolder=user, image=os.path.join("static/scotland.png"))
    scotland.save()

    twitter = Product(category="COOPERATION", title="Scotland", price="50000000", description="It pays to be verified nowadays, buy if off Eron Mask now",
                       seller=user, currentHolder=user, image=os.path.join("static/twitter.png"))
    twitter.save()


def home(request):
    homePage = "HOME.html"
    if request.user.is_authenticated:
        product_list = Product.objects.all()
        return render(request, homePage, {"product_list": product_list})
    else:
        return redirect(register)


def register(request):
    """
        return rendered sign in page

        Args:
            request: request send from user

        Returns:
            render(html): rendered signup page
    """
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        rePassword = request.POST['repassword']
        # add database connection
        if password != rePassword:
            return render(request, "register.html", {'error': "password dont match"})
        try:
            # create a user instance
            user = User.objects.create_user(username=userName, password=password)
            user.save()
            print("Registration completed")
            loginSuccess = authenticate(request, username=userName, password=password)
            login(request, loginSuccess)
            return redirect('/home/')
        except IntegrityError:
            return render(request, "register.html", {'error': "Account Error: Account has been registered"})
    else:
        return render(request, "register.html", {})


def signin(request):
    """
        when received request from user, return user a page with sign-in status update

            Args:
               request: send from user

            Returns:
                render(request): rendered sign-in html page
    """
    if request.method == "POST":
        userName = request.POST['username']
        password = request.POST['password']
        print("user " + userName + " attempt to log")
        loginSuccess = authenticate(request, username=userName, password=password)
        print("Profile created")
        if loginSuccess is None:
            return render(request, "signin.html", {"error": "USER NAME AND PASSWORD DONT EXIST"})
        else:
            login(request, loginSuccess)
            return redirect('/home/')
    else:
        return render(request, "signin.html")


@login_required
def logout(request):
    auth.logout(request)
    return redirect("/home/")


@login_required
def uploadProduct(request):
    """
        when received product information sent by user, stored in the database and document in the media folder

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    uploadHTML = "uploadProduct.html"

    if request.method == "POST":

        userName = request.user.username
        productName = request.POST["productName"]
        productPrice = request.POST["price"]
        productDescription = request.POST["description"]
        category = request.POST['category']
        uploadFile = request.FILES['productPicture']

        # create folder for user
        fileStorage = FileSystemStorage()
        parent = fileStorage.location
        # change tuple type to string(userName is tuple)
        username = ''.join(userName)
        directory = username
        path = os.path.join(parent, directory)
        # if user folder doesn't exist create folder for user
        if not os.path.exists(path):
            os.mkdir(path)
            print(username + " folder created ")

        productInstance = Product(
            seller=request.user,
            currentHolder=request.user,
            title=productName,
            price=productPrice,
            description=productDescription,
            category=category,
        )
        productInstance.save()
        print("PRODUCT ADDED INTO DATABASE")

        # save image on local machine
        itemID = str(productInstance.productID)
        fileStorage.save(username + "/" + itemID + ".jpg", uploadFile)

        # get product info
        product = Product.objects.filter(seller=request.user, title=productName)[0]
        itemID = str(product.productID)

        # update product image
        Product.objects.filter(seller=request.user, productID=itemID).update(seller=request.user,
                                                                             currentHolder=request.user,
                                                                             title=productName,
                                                                             image=username + "/" + itemID + ".jpg",
                                                                             price=productPrice,
                                                                             description=productDescription,
                                                                             category=category, )

        return render(request, uploadHTML, {"error": "Item has added"})

    return render(request, uploadHTML)


def click_bid(request):
    data = json.loads(request.body)
    productId = data['productId']
    request.session['productID'] = productId

    if request.method == 'POST':
        return redirect('/product_page/')
    else:
        return render(request, 'account.html')


@login_required
def productPage(request, productID):
    """
    :param productID: productID
    :param request:
    :return:
    """
    bidPageHtml = "bidpage.html"

    product = Product.objects.filter(productID=productID)[0]
    seller = product.seller
    productName = product.title
    productPrice = product.price
    productImageUrl = product.image.url
    productDescription = product.description
    productSeller = product.seller
    minBid = productPrice + 1
    context = {"name": productName, "price": productPrice, "image": productImageUrl, "description": productDescription,
               "seller": productSeller, "minBid": minBid,"productID": productID}

    if request.method == "POST":
        newBid = request.POST['newBid']
        if int(newBid) <= int(productPrice):
            context["notification"] = "MUST BE HIGHER THAN CURRENT BID"
            return render(request, bidPageHtml, context)
        else:
            context["notification"] = "CONGRATS, YOU ARE THE HIGHEST BIDDER"

            currentBidder = request.user
            # bid successful, update database
            Product.objects.filter(productID=productID).update(price=newBid,
                                                               currentHolder=currentBidder)
            return render(request, bidPageHtml, context)
    else:
        return render(request, bidPageHtml, context)



@login_required
def NFTPage(request):
    homePage = "HOME.html"
    NFT_product_list = Product.objects.filter(category="NFT").all()
    return render(request, homePage, {"product_list": NFT_product_list})


@login_required
def NFTPage(request):
    homePage = "HOME.html"
    NFT_product_list = Product.objects.filter(category="NFT").all()
    return render(request, homePage, {"product_list": NFT_product_list})


@login_required
def BlockChainPage(request):
    homePage = "HOME.html"
    BlockChain_product_list = Product.objects.filter(category="BlockChain").all()
    return render(request, homePage, {"product_list": BlockChain_product_list})


@login_required
def MetaVersePage(request):
    homePage = "HOME.html"
    MetaVerse_product_list = Product.objects.filter(category="MetaVerse").all()
    return render(request, homePage, {"product_list": MetaVerse_product_list})



@login_required
def LandPage(request):
    homePage = "HOME.html"
    Land_product_list = Product.objects.filter(category="Land").all()
    return render(request, homePage, {"product_list": Land_product_list})


@login_required
def COOPERATIONPage(request):
    homePage = "HOME.html"
    COOPERATION_product_list = Product.objects.filter(category="COOPERATION").all()
    return render(request, homePage, {"product_list": COOPERATION_product_list})


@login_required
def PlanetPage(request):
    homePage = "HOME.html"
    Planet_product_list = Product.objects.filter(category="Planet").all()
    return render(request, homePage, {"product_list": Planet_product_list})


@login_required
def VehiclePage(request):
    homePage = "HOME.html"
    Vehicle_product_list = Product.objects.filter(category="Vehicle").all()
    return render(request, homePage, {"product_list": Vehicle_product_list})


@login_required
def CameraPage(request):
    homePage = "HOME.html"
    Camera_product_list = Product.objects.filter(category="Camera").all()
    return render(request, homePage, {"product_list": Camera_product_list})


@login_required
def LensesPage(request):
    homePage = "HOME.html"
    Lenses_product_list = Product.objects.filter(category="Lenses").all()
    return render(request, homePage, {"product_list": Lenses_product_list})


@login_required
def ComputerPage(request):
    homePage = "HOME.html"
    Computer_product_list = Product.objects.filter(category="Computer").all()
    return render(request, homePage, {"product_list": Computer_product_list})


@login_required
def CollabPage(request):
    homePage = "HOME.html"
    Collab_product_list = Product.objects.filter(category="Collab").all()
    return render(request, homePage, {"product_list": Collab_product_list})


