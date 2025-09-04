
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    contexto = {
        "titulo": "Blog - Página Inicial",
        "mensagem": "Conteúdo vindo da view (Python) para o template."
    }
    return render(request, "blog/index.html", contexto)

def sobre(request):
    return render(request, "blog/sobre.html", {"titulo": "Sobre o Blog", "autor": "Professor & Erick"})

def detalhe(request, post_id: int):
    # Exemplo simples usando parâmetro dinâmico (sub-rota)
    return render(request, "blog/detalhe.html", {"titulo": f"Post #{post_id}", "post_id": post_id})
