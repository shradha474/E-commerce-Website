from django.conf.urls import url
from website import views
from django.conf.urls.static import static, settings
from .models import Products, Index_skirts, Index_watch, Index_dress, Index_sweaters
from django.contrib import admin
from .forms import UserForm


urlpatterns = [
url(r'^$', views.homepageview, name= 'index'),

url(r'^registration/$', views.UserFormView.as_view(), name= 'register'),
url(r'^registration/login$', views.login_user, name= 'login'),



url(r'^about/$', views.aboutview.as_view(), name='about'),

url(r'^checkout/$', views.checkoutview.as_view(), name='checkout'),

url(r'^dress/$', views.dressview.as_view(), name='dress'),



url(r'^faq/$', views.faqview.as_view(), name='faq'),

url(r'^jeans/$', views.jeansview.as_view(), name='jeans'),

url(r'^mail/$', views.mailview.as_view(), name='mail'),

url(r'^products/$', views.productsview.as_view(), name='products'),

url(r'^salwars/$', views.salwarsview.as_view(), name='salwars'),

url(r'^sandal/$', views.sandalsview.as_view(), name='sandals'),

url(r'^sarees/$', views.sareesview.as_view(), name='sarees'),

url(r'^shirts/$', views.shirtsview.as_view(), name='shirts'),

url(r'^kids-wear/$', views.kidswearview.as_view(), name='kidswear'),



url(r'^ skirts/$', views. skirtsview.as_view(), name='skirts'),

url(r'^sweaters/$', views.sweatersview.as_view(), name='sweaters'),



url(r'^single/(?P<pk>[0-9]+)/$', views.singleView, name='single'),
url(r'^single//(?P<pk>[0-9]+)/$', views.single_sweaterView, name='single_sweater'),
url(r'^single///(?P<pk>[0-9]+)/$', views.single_skirtsView, name='single_skirts'),
url(r'^single///(?P<pk>[0-9]+)//$', views.single_jeansView, name='single_jeans'),
url(r'^single////(?P<pk>[0-9]+)/$', views.single_shirtsView, name='single_shirts'),
url(r'^single////(?P<pk>[0-9]+)//$', views.productsView, name='single_products'),
url(r'^single/(?P<pk>[0-9]+)//$', views.single_salwarsView, name='single_salwars'),
url(r'^single/(?P<pk>[0-9]+)///$', views.single_sareesView, name='single_sarees'),
url(r'^single//(?P<pk>[0-9]+)//$', views.single_sandalsView, name='single_sandals'),
url(r'^single//(?P<pk>[0-9]+)///$', views.single_indexView, name='single_index'),
url(r'^single/(?P<pk>[0-9]+)////$', views.single_kidsView, name='single_kids'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
