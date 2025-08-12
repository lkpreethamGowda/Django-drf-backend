from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router=DefaultRouter()
router.register(r'farmers',views.FarmerViewset) # Farmer Crud operation
router.register(r'users',views.UserViewset)  # User Crud Operation 
router.register(r'discounts',views.DiscountViewset) # returns or GET a coupon using the coupon value
router.register(r'products',views.ProductViewset) #Producs Crud operation
router.register(r'reviews',views.ReviewViewset) # creates and retrievees the revies for the perticular product
router.register(r'carts',views.CartViewset) #Gets the cart based on the user_id and  used for creating a single cart for user when user is signed in 
router.register(r'cartItems',views.CartItemViewset , basename='cartItems') # returns cartitems based on cart_id
router.register(r'addToCarts',views.AddtoCart, basename= 'addToCart') #Adds to cart by using user ID to get the Cart_id
router.register(r'orders',views.OrderViewset)# reuturns the orders with respect to User_ID
router.register(r'addorders',views.OrderAddViewset, basename="addOrder")  # Adding orders
router.register(r'searchProducts',views.ProductSearchViewset, basename="searchProducts")# search the product based on product_name and filter = label,type and price range
router.register(r'recipes',views.RecipeViewset, basename='recipes') 
router.register(r'DeleteCartItem',views.DeleteCartItem, basename="DeleteCartItem") # delete the cartItem





urlpatterns=[
  
]
urlpatterns+=router.urls

""" path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),"""