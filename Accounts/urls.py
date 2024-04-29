from django.urls import path
from Accounts.views import login_page,register_page


urlpatterns = [
   path('login/', login_page , name="login"),
   path('register/' , register_page , name="register"),
   

]