from django.conf.urls import url
import views

app_name = 'analyser'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home', views.seller_home, name='home'),
    url(r'^ajax/addItem', views.addItem, name='addItem'),
]