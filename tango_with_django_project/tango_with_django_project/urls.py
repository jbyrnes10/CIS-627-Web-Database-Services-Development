from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import password_change, password_change_done

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/password/change/$', password_change,
        {'template_name': 'registration/password_change_form.html'},
        name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done,
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)