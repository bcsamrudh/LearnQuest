from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.about,name="about"),
    path('user/',include('user.urls')),
    path('notes/',include('notes.urls')),
    path("unicorn/", include("django_unicorn.urls")),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)