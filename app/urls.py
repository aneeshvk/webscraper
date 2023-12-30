from django.urls import path
from .import views



urlpatterns = [
    path('' ,views.function,name='function'),
    path('login/',views.app,name='app'),
    path('level2', views.login_level2_student, name="login_level2_student"),
    path('register/',views.register,name='register'),
    path('clogin/',views.app_app,name='app_app'),
    path('cregister/',views.cregister,name='cregister'),
    path('ngoregister/',views.ngoregister,name='ngoregister'),
    path('glogin/',views.glogin,name='glogin'),
    path('ngo/', views.ngologin, name='ngologin'),
    path('usignin/',views.usignin,name='usignin'),
    path('csignin/',views.csignin,name='csignin'),
    path('userview/',views.userviews,name='userviews'),
    path('cview/',views.cviews,name='cviews'),
    path('gvtview/',views.gviews,name='gviews'),
    path('uregister/',views.uregister,name='uregister'),
    path('home/',views.home,name='home'),
    path('home1/',views.home1,name='home1'),
    # path('Application/',views.Application,name='Application')
    path('home2/',views.home2,name='home2'),
    path('userupload/',views.userupload,name='userupload'),
    path('allngo/', views.allngo, name='useruallngo'),
    path('ngodelete/<int:id>', views.ngo_delete, name='ngo_delete'),
    path('allcreg/', views.allcreg, name='allcreg'),
    path('allureg/', views.allureg, name='allureg'),
    path('councillorupload/',views.councillorupload,name='councillorupload'),
    path('changestatus/<int:customer_id>', views.changestatus_customer, name='changestatus_user'),
    path('updateureg/', views.update_ureg, name='updateureg'),
    path('dosraping/', views.do_sraping, name='dosraping'),
    path('delete/<int:customer_id>', views.delete_ureg, name='delete_ureg'),
  

]