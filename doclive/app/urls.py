from django.urls import path
from .views import ItemList, ItemDetail, LocationDetail, LocationList, SignUp, Login, Dashboard, Logout

urlpatterns = [
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('signup/', SignUp.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('dashboard/', Dashboard.as_view()),
]