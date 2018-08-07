from django.conf.urls import url
from projectapp import views
urlpatterns=[
url(r'^storeappsinup$',views.StoreSingup.as_view(),name='StoreSingup'),
url(r'^storeapplogin$',views.StoreLogin.as_view(),name='StoreLogin'),
url(r'^inventorylist$',views.Inventorylist.as_view(),name='Inventorylist'),
url(r'^addinventory$',views.AddInventoryRecord.as_view(),name='AddInventoryRecord'),
url(r'^inventoryapporove$',views.Approve.as_view(),name='Approve'),
]

