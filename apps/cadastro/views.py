from django.shortcuts import render, redirect, get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import ServidorForm
from .models import Servidor
from django.contrib import messages
import csv

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


@login_required(login_url="/login/")
def delServidor(request, id):
    servidor = get_object_or_404(Servidor, pk=id)
    servidor.delete()
    messages.success(request, 'Servidor deletado com sucesso.')
    return redirect('list-cadastro')


@login_required(login_url="/login/")
def editServidor(request, id):
    servidor = get_object_or_404(Servidor, pk=id)
    form = ServidorForm(instance=servidor)

    if request.method == 'POST':
        form = ServidorForm(request.POST or None, instance=servidor)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro atualizado com Sucesso')
            return redirect('list-cadastro')
        else:
            return render(request, 'cadastro/editservidor.html', {'form': form})
    else:
        return render(request, 'cadastro/editservidor.html', {'form': form})



@login_required(login_url="/login/")
def export_csv(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['cpf', 'nome', 'dt_nascimento', 'sexo', 'nome_pai', 'nome_mae', 'nascionalidade', 'ano_brasil', 'dt_naturalizacao', 'municipio_naturalizacao',
                     'uf_naturalizacao', 'estado_civil', 'raca', 'tipo_deficiencia', 'rg', 'orgao_emisso', 'uf_rg', 'dt_expedicao_rg', 'email', 'endereco',
                     'numero_residencia', 'complemento_residencia', 'bairro', 'cidade', 'uf', 'cep', 'tel_fixo', 'tel_celular', 'num_reservista', 'orgao_emissor_reservista',
                     'dt_emissao_reservista', 'uf_reservista', 'titulo_eleitor', 'zona_eleitor', 'secao_eleitor', 'dt_emissao_titulo', 'cidade_titulo',
                     'num_habilitacao', 'cat_habilitacao', 'uf_habilitacao', 'dt_primeira_habilitacao', 'dt_validade_habilitacao', 'dt_primeiro_emprego', 'dt_final_emprego',
                     'nome_empresa', 'tipo_sanguineo', 'fator_rh', 'num_rne', 'emissor_rne', 'dt_emissao_rne', 'clas-trabalho', 'ctps_n', 'serie_ctps', 'estado_ctps',
                     'dt_emissao_ctps', 'matricula', 'dt_admissao', 'dt_desligamento', 'dt_posse', 'portador_pne', 'cargo', 'tipo_cargo', 'funcao', 'especialidade',
                     'relacao_trabalho', 'regime_trabalho', 'tipo_vinculo', 'nivel_salario', 'carga_horaria', 'banco', 'agencia', 'conta'])

    servidores = Servidor.objects.filter()

    for servidor in servidores:
      writer.writerow([servidor.cpf, servidor.nome, servidor.dt_nascimento, servidor.sexo, servidor.nome_pai, servidor.nome_mae, servidor.nascionalidade,
                       servidor.ano_brasil, servidor.dt_naturalizacao, servidor.municipio_naturalizacao, servidor.uf_naturalizacao, servidor.estado_civil,
                       servidor.raca, servidor.tipo_deficiencia, servidor.rg, servidor.orgao_emisso, servidor.uf_rg, servidor.dt_expedicao_rg, servidor.email,
                       servidor.endereco, servidor.numero_da_residencia, servidor.complemento_da_residencia, servidor.bairro, servidor.cidade, servidor.uf,
                       servidor.cep, servidor.tel_fixo, servidor.tel_celular, servidor.num_reservista, servidor.orgao_emisso_reservista, servidor.dt_emissao_reservista,
                       servidor.uf_reservista, servidor.titulo_eleitor, servidor.zona_eleitor, servidor.secao_eleitor, servidor.dt_emissao_titulo, servidor.cidade_titulo,
                       servidor.num_habilitacao, servidor.cat_habilitacao, servidor.uf_habilitacao, servidor.dt_primeira_habilitacao, servidor.dt_validade_habilitacao,
                       servidor.dt_primeiro_emprego, servidor.dt_final_emprego, servidor.nome_empresa, servidor.tipo_sanguineo,
                       servidor.fator_rh, servidor.num_rne, servidor.emissor_rne, servidor.dt_emissao_rne, servidor.clas_trabalho, servidor.ctps_n, servidor.serie_ctps,
                       servidor.estado_ctps, servidor.dt_emissao_ctps, servidor.matricula, servidor.dt_admissao, servidor.dt_desligamento, servidor.dt_posse,
                       servidor.portador_pne, servidor.cargo, servidor.tipo_cargo, servidor.funcao, servidor.especialidade, servidor.relacao_trabalho,
                       servidor.regime_trabalho, servidor.tipo_vinculo, servidor.nivel_salario, servidor.carga_horaria, servidor.banco, servidor.agencia, servidor.conta])

    return response