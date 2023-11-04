from django .urls import path
from account.views import home,signup,user_login,profile,user_logout,pass_change
urlpatterns = [
    path('', home),
    path('signup/',signup, name='signup'),
    path('login/',user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_pass/', pass_change, name='pass_change'),
    path('profile/',profile,name='profile'),
]
