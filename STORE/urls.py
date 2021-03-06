from django.urls import path
from .views import *
from . import views 
app_name="STORE"
# from allauth import urls 

urlpatterns = [
path("",views.home,name="home"),
path("test/",views.test,name="test"),
 
#main pages
path("products/",views.products,name="products"),
path("category/<str:slug>/",views.category,name="category_filter"),
path("branch/<str:slug>/",views.branch,name="branch_filter"),

path("wishlist/",views.wishlist,name="wishlist"),

path("product/<str:id>/",views.this_product,name="this_product"),
path("cart/",views.cart,name="cart"),
path("order/<str:id>/",views.order,name="order"),
path("order/<str:id>/confirm/",views.order_confirm,name="order_confirm"),
path("empty/",views.empty,name="empty"),   
path("account/<str:slug>/",views.profile,name="profile"), 
path("profile/<str:slug>/",views.profile_account,name="profile_account"),   
path("profile/<str:slug>/edit",views.profile_edit,name="profile_edit"),   

path("address/<str:slug>/",views.address,name="address"),   
path("address/add/<str:slug>/",views.address_add,name="address_add"),   
path("orders/<str:slug>/",views.order_track,name="order_track"),        
path("order/user/<str:slug>/<str:id>/",views.manage_order,name="manage_order"),     
path("canceled/order/<str:slug>/",views.canceled_order,name="canceled_order"),         
path("FAQ/",views.faq,name="faq"),         
path("about/",views.about,name="about"),            
path("contact/",views.contact,name="contact"),  
path("search/",views.search,name="search"),
path("blogs/",views.blogs,name="blogs"),
path("sucess/",views.success,name="success"),
     

## news
path("news/",views.news,name="news"),            
  
#sessions_delete
path("shiiping/delete",views.shipping_session,name="shipping_delete"),
path("price/delete",views.price_session,name="price_session_delete"),
path("rate/delete",views.rating_session,name="rating_session_delete"),
path("manu/delete",views.manu_session,name="manu_session_delete"),
path("size/delete",views.size_session,name="size_session_delete"),


# Cart
path("add-to-cart/",views.add_to_cart,name="cart_add"),
path("quick-add/<str:id>/",views.quick_add,name="quick_add"),
path("remove-from-cart/",views.remove_from_cart,name="cart_remove"),
path("whislist-add/",views.wishlist_add,name="wishlist_add"),
path("whislist-remove/",views.wishlist_remove,name="wishlist_remove"),
path("quantity/add/<str:id>/",views.quantity_add,name="quantity_add"),
path("cart/clear/",views.cart_clear,name="cart_clear"),
path("whislist-list-remove/",views.wishlist_list_remove,name="wishlist_list_remove"),
path("make_primary/",views.make_primary,name="make_primary"),
path("make-new-address/",views.make_new_address,name="make_new_address"),
path("address_edit/<str:id>/",views.address_edit,name="address_edit"),  
path("make-payment-option/",views.make_payment_option,name="make_payment_option"),
path("quantity_add/",views.cart_quantity_add,name="cart_quantity_add"),
path("quantity_remove/",views.cart_quantity_remove,name="cart_quantity_remove"),
path("coupon/",views.coupon,name="coupon"),
path("shipping/<str:id>/",views.shipping_cost,name="shipping"),
     
    
### PAYMNETS     

path("create/<str:id>/",views.create,name="create"),  
path("capture/<str:order_id>/<str:id>/",views.capture,name="capture"),  
#       Dashboard              
path("dashboard/",views.dashboard,name="dashboard"),
path("dashboard/orders/",views.dash_orders,name="dash_orders"),
path("dashboard/orders/<str:id>/",views.dash_order_details,name="dash_order_details"),
path("dashboard/products/add",views.add_products,name="products_add"),
path("dashboard/products/modify/<str:id>/",views.modify_product,name="products_modify"),
path("dashboard/products/delete_product/<str:id>/",views.delete_product,name="product_delete"),
path("dashboard/deals/",views.deals,name="deals"),
path("dashboard/deals/add/",views.deals_add,name="deals_add"),
path("dashboard/deals/delete/<str:id>/",views.deals_delete,name="deals_delete"),
path("dashboard/category/",views.category_dash,name="category"),
path("dashboard/category/add/",views.category_add,name="category_add"),
path("dashboard/category/delete/<str:id>/",views.category_delete,name="category_delete"),
path("dashboard/branch/",views.dashboard_branch,name="branch"),
path("dashboard/branch/add/",views.branch_add,name="branch_add"),
path("dashboard/branch/delete/<str:id>/",views.branch_delete,name="branch_delete"),
path("dashboard/manu/",views.manu,name="manu"),
path("dashboard/manu/add/",views.manu_add,name="manu_add"),
path("dashboard/manu/delete/<str:id>/",views.manu_delete,name="manu_delete"),


]             
         
 