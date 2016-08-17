from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from accounts import urls as accountsUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accountsUrls)),
]
