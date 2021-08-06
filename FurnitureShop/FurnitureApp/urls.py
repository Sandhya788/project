from django.urls import path
from FurnitureApp import views
from FurnitureApp.views import Home
from django.contrib.auth import views as v

urlpatterns = [
	path('abt/',views.about,name='ab'),	
	path('cntct/',views.contact,name='ct'),
	path('rlist/',views.restlist,name="rstl"),
	path('rstup/<int:m>/',views.rstup,name='rsup'),
	path('dd/<int:s>/',views.rstdl,name='rsdl'),
	path('rstviw/<int:a>/',views.rstvw,name="rsvw"),
	path('ritems/',views.ritems,name="ritms"),
	path('itmup/<int:p>/',views.itemupt,name="imup"),
	path('itmdl/<int:v>/',views.itemdel,name="imdl"),
	path('itmvw/<int:y>/',views.itemviw,name="imvw"),
	path('rg/',views.usrreg,name='reg'),
	path('login/',v.LoginView.as_view(template_name="app/login1.html"),name='lg'),
	path('logout/',v.LogoutView.as_view(template_name="app/logout.html"),name='lg1'),
	path('roltype/',views.rolereq,name="rlrq"),
	path('gvper/',views.gveperm,name="gvpm"),
	path('gvup/<int:t>/',views.gvupd,name='gvup'),
	path('pfle/',views.pfle,name='pf'),
	path('fdb',views.feedback,name='fd'),
	path('pfud/',views.pfleupd,name="pfup"),
	path('chge/',views.changepwd,name='chpd'),
	path('orders/',views.forders,name='fo'),
	path('cart/',views.cart,name='ca'),
	path('', Home.as_view(), name='hm')
	# path('ch',views.check,name='chi'),
]