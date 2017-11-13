"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from instruments.views import InstrumentList, InstrumentDetail


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.aboutUS, name='aboutUS'),
    url(r'^contact$', views.ContactUS, name='ContactUS'),
    url(r'^register$', views.Register, name='Register'),
    url(r'^specs$', views.specs, name='specs'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^transactions$', views.transaction, name='transactions'),
    url(r'^funds$', views.funds, name='funds'),
    url(r'^deposits$', views.deposits, name='deposits'),
    # url(r'^payments$', views.CheckoutView, name='payments'),
    url(r'^instruments/$', InstrumentList.as_view(), name="instrument_list"),
    url(r'^instruments/detail/(?P<pk>\d+)/$', InstrumentDetail.as_view(), name='instrument_detail'),
    url(r'^instruments/detail/(?P<slug>[-\w]+)/$', InstrumentDetail.as_view(), name='instrument_detail_slug'),
    #url(r'^cart/$', CartView.as_view(),name= 'cart'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^instrument/purchase/$',views.purchase_made,name = "purchase_made"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
