# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.cadastro import views

urlpatterns = [

    path('', views.index, name='home'),
    path('listcadastro/', views.listCadastro, name='list-cadastro'),
    path('addservidor/', views.addServidor, name='add-servidor'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
