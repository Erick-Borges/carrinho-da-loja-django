
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home</h1><p>Bem-vindo à Aula 09 (Django)!</p><p>Vá para <a href='/blog/'>/blog/</a></p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', include('blog.urls')),
]
