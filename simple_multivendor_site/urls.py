
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/', core_views.Login, name='login'),
    path('logout/', core_views.frontpage, name='logout'),
    path('register/', core_views.register, name='register'),
    path('vendor/', include('vendor.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
