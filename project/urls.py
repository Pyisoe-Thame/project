"""
URL configuration for my_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from shop.admin import shop_site

urlpatterns = [
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls, name='name'),
    path('shop-admin/', shop_site.urls, name='shop_admin'),  # urls for shop admin area
    path('', include('shop.urls')),

    # Place the catch-all pattern at the end
    path('static/<path:path>', include('django.contrib.staticfiles.urls')),
    path('<path:path>', include('django.contrib.staticfiles.urls')),  # Catch-all pattern
]

# admin.site.index_title = "Artificial Heirlooms"
# admin.site.site_header = "Artificial Heirlooms Admin"
# admin.site.site_title = "Site Title Artificial Heirlooms"

