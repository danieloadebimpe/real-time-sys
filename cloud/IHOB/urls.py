from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path("logout/", views.logout),
    path('home/', views.home),
    path("signin/", views.signin),
    path('uploadProduct/', views.uploadProduct),
    path('bid_click/', views.click_bid),
    path('product_page/<str:productID>', views.productPage),
    path('NFT/', views.NFTPage),
    path("BlockChain/", views.BlockChainPage),
    path('MetaVerse/', views.MetaVersePage),
    path('Land/', views.LandPage),
    path('COOPERATION', views.COOPERATIONPage),
    path('Planet/', views.PlanetPage),
    path("Vehicle/", views.VehiclePage),
    path('Camera/', views.CameraPage),
    path('Lenses/', views.LensesPage),
    path('Computer/', views.ComputerPage),
    path('Collab/', views.CollabPage)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)