from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from .forms import LoginForm, SignUpForm

from .models import (
    CotacoesDasAcoes,
)

from .serializers import (
    CompanySerializer,
    CotacoesDasAcoesSerializer,
)

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("/index.html")

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "home/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("home/index.html")

        else:
            msg = "Dados invalidos"
    else:
        form = SignUpForm()

    return render(
        request, "home/register.html", {"form": form, "msg": msg, "success": success}
    )


# @login_required(login_url="/login/")
def index(request):
    lista = CotacoesDasAcoes.objects.all()
    context = {
        "segment": index,
        "lista": lista,
    }

    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split("/")[-1]

        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))


