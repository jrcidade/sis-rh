from django.shortcuts import render, redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import ServidorForm
from .models import Servidor
from django.contrib import messages


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index3.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def listCadastro(request):
    servidores = Servidor.objects.all()
    return render(request, 'cadastro/listcadastro.html', {'servidores': servidores})


@login_required(login_url="/login/")
def addServidor(request):
    if request.method == 'POST':
        form = ServidorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Servidor cadastrado com sucesso.')
            return redirect('list-cadastro')
        else:
            messages.error(request, 'Servidor ja esta cadastrado no Sistema.')
            return redirect('list-cadastro')

    else:
        form = ServidorForm()
        return render(request, 'cadastro/addservidor.html', {'form': form})

