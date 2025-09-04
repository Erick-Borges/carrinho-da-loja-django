
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),              # /blog/
    path("sobre", views.sobre, name="sobre"),         # /blog/sobre
    path("algo", views.detalhe, {"post_id": 1}, name="algo"),   # sub-rota fixa como exemplo
    path("outro", views.detalhe, {"post_id": 2}, name="outro"), # sub-rota fixa como exemplo
    path("post/<int:post_id>", views.detalhe, name="post"),     # /blog/post/42
]
