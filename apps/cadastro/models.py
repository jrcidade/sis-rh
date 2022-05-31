from django.db import models


class Servidor(models.Model):

    SEXO = (
        ('MASCULINO', 'MASCULINO'),
        ('FEMININO', 'FEMININO'),
    )

    UF = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins'),
    )

    NACIONALIDADE = (
        ('BRASILEIRO', 'BRASILEIRO'),
        ('BRASILEIRA', 'BRASILEIRA'),
        ('ESTRANGEIRO', 'ESTRANGEIRO'),
        ('ESTRANGEIRA', 'ESTRANGEIRA'),
    )

    ESTADO_CIVIL = (
        ('CASADO', 'CASADO'),
        ('CASADA', 'CASADA'),
        ('SOLTEIRO', 'SOLTEIRO'),
        ('SOLTEIRA', 'SOLTEIRA'),
        ('DIVORCIADO', 'DIVORCIADO'),
        ('DIVORCIADA', 'DIVORCIADA'),
        ('VIÚVO', 'VIÚVO'),
        ('VIÚVA', 'VIÚVA'),
    )
    RACA = (
        ('BRANCA', 'BRANCA'),
        ('PRETA', 'PRETA'),
        ('AMARELA', 'AMARELA'),
        ('PARDA', 'PARDA'),
        ('INDÍGENA', 'INDÍGENA'),
        ('SEM DECLARAÇÃO', 'SEM DECLARAÇÃO'),
    )
    TIPO_DEFICIENCIA = (
        ('DEFICIÊNCIA VISUAL', 'DEFICIÊNCIA VISUAL'),
        ('DEFICIÊNCIA MOTORA', 'DEFICIÊNCIA MOTORA'),
        ('DEFICIÊNCIA MENTAL', 'DEFICIÊNCIA MENTAL'),
        ('DEFICIÊNCIA AUDITIVA', 'DEFICIÊNCIA AUDITIVA'),
        ('PARALISIA CEREBRAL', 'PARALISIA CEREBRAL'),
    )

    TIPO = (
        ('NÃO', 'NÃO'),
        ('SIM', 'SIM'),
    )

    TIPO_CARGO = (
        ('EFETIVO', 'EFETIVO'),
        ('COMISSIONADO', 'COMISSIONADO'),
        ('FEDERAL', 'FEDERAL'),
        ('CLT', 'CLT'),
    )

    RELACAO_TRABALHO = (
        ('ACT - ADMITIDO EM CARÁTER TEMPORÁRIO', 'ACT - ADMITIDO EM CARÁTER TEMPORÁRIO'),
        ('EFETIVO', 'EFETIVO'),
        ('MILITAR', 'MILITAR'),
        ('À DISPOSIÇÃO', 'À DISPOSIÇÃO'),
        ('CTISP', 'CTISP'),
        ('AGENTE POLÍTICO', 'AGENTE POLÍTICO'),
        ('COMISSIONADO', 'COMISSIONADO'),
        ('CONSELHEIRO', 'CONSELHEIRO'),
        ('DIRETOR/PRESIDENTE', 'DIRETOR/PRESIDENTE'),
        ('FTG - FUNÇÃO TÉCNICA GERENCIAL', 'FTG - FUNÇÃO TÉCNICA GERENCIAL'),
        ('FG - FUNÇÃO GRATIFICADA', 'FG - FUNÇÃO GRATIFICADA'),
    )

    REGIME_TRABALHO = (
        ('CLT', 'CLT'),
        ('ESTATUTÁRIO', 'ESTATUTÁRIO'),
        ('ADMINISTRATIVO ESPECIAL', 'ADMINISTRATIVO ESPECIAL'),
        ('NÃO QUALIFICADO', 'NÃO QUALIFICADO'),
        ('EXCEDENTE', 'EXCEDENTE'),
        ('CONTRIBUINTE INDIVIDUAL', 'CONTRIBUINTE INDIVIDUAL'),
        ('VOLUNTÁRIO', 'VOLUNTÁRIO'),
    )

    TIPO_VINCULO = (
        ('CARGO PERMANENTE', 'CARGO PERMANENTE'),
        ('CARGO TEMPORÁRIO', 'CARGO TEMPORÁRIO'),
        ('EMPREGO PERMANENTE', 'EMPREGO PERMANENTE'),
        ('EMPREGO TEMPORÁRIO', 'EMPREGO TEMPORÁRIO'),
        ('FUNÇÃO PÚBLICA TEMPORÁRIA', 'FUNÇÃO PÚBLICA TEMPORÁRIA'),
        ('PENSIONISTA', 'PENSIONISTA'),
        ('FUNÇÃO PÚBLICA ESPECIAL', 'FUNÇÃO PÚBLICA ESPECIAL'),
        ('SERVIÇO VOLUNTÁRIO', 'SERVIÇO VOLUNTÁRIO'),
    )

    cpf = models.CharField(max_length=14, verbose_name="Cpf nº.", help_text="Somente os números", unique=True)
    nome = models.CharField(max_length=250, verbose_name="Nome Servidor(a)")
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento", help_text="Somente os números")
    sexo = models.CharField(max_length=12, choices=SEXO, verbose_name="Sexo")
    nome_pai = models.CharField(max_length=250, verbose_name="Nome completo do Pai", null=True, blank=True)
    nome_mae = models.CharField(max_length=250, verbose_name="Nome completo da Mãe", null=True, blank=True)
    nascionalidade = models.CharField(max_length=15, choices=NACIONALIDADE, verbose_name='Nascionalidade')
    ano_brasil = models.DateField(verbose_name="Ano Chegada no País", help_text="No formato: AAAA", null=True, blank=True)
    dt_naturalizacao = models.DateField(verbose_name="Data Naturalização", help_text="Somente os números", null=True, blank=True)
    municipio_naturalizacao = models.CharField(max_length=250, verbose_name="Municipio Naturalização", null=True, blank=True)
    uf_naturalizacao = models.CharField(max_length=20, choices=UF, null=True, verbose_name='UF de Naturalização', blank=True)
    estado_civil = models.CharField(max_length=15, choices=ESTADO_CIVIL, verbose_name='Estado Civil', null=True, blank=True)
    raca = models.CharField(max_length=15, choices=RACA, verbose_name='Raça', null=True, blank=True)
    tipo_deficiencia = models.CharField(max_length=20, choices=TIPO_DEFICIENCIA, null=True, verbose_name='Tipo Deficiência', blank=True)
    rg = models.CharField(max_length=100, verbose_name='RG nº')
    orgao_emisso = models.CharField(max_length=20, verbose_name='Orgão Emissor', null=True, blank=True)
    uf_rg = models.CharField(max_length=20, choices=UF, verbose_name='UF Emissor', null=True, blank=True)
    dt_expedicao_rg = models.DateField(verbose_name="Data de Expedição do RG", help_text="Somente os números", null=True, blank=True)
    email = models.CharField(max_length=150, verbose_name='Email:', null=True, blank=True)
    endereco = models.CharField(max_length=250, verbose_name='Endereço', null=True, blank=True)
    numero_da_residencia = models.CharField(max_length=10, verbose_name='Número da residencia', null=True, blank=True)
    complemento_da_residencia = models.CharField(max_length=150, verbose_name='Complemento', null=True, blank=True)
    bairro = models.CharField(max_length=15, verbose_name='Bairro', null=True, blank=True)
    cidade = models.CharField(max_length=20, verbose_name='Cidade', null=True, blank=True)
    uf = models.CharField(max_length=2, choices=UF, verbose_name='UF.', null=True, blank=True)
    cep = models.CharField(max_length=15, verbose_name='Cep. ', help_text='Somente os números', null=True, blank=True)
    tel_fixo = models.CharField(max_length=20, verbose_name='Telefone Fixo', help_text='Somente os números', null=True, blank=True)
    tel_celular = models.CharField(max_length=20, verbose_name='Celular', help_text='Somente os números', null=True, blank=True)
    num_reservista = models.CharField(max_length=50, verbose_name='Número Reservista', null=True, blank=True)
    orgao_emisso_reservista = models.CharField(max_length=50, verbose_name='Orgão Emissor Reservista', null=True, blank=True)
    dt_emissao_reservista = models.DateField(verbose_name="Data de Expedição do Reservista", help_text="Somente os números", null=True, blank=True)
    uf_reservista = models.CharField(max_length=2, choices=UF, verbose_name='UF. Reservista', null=True, blank=True)
    titulo_eleitor = models.CharField(max_length=20, verbose_name='Titulo Eleitor', help_text='Somente os números', null=True, blank=True)
    zona_eleitor = models.CharField(max_length=20, verbose_name='Zona Eleitor', null=True, blank=True)
    secao_eleitor = models.CharField(max_length=20, verbose_name='Seção Eleitor', null=True, blank=True)
    dt_emissao_titulo = models.DateField(verbose_name="Data de Expedição do titulo", help_text="Somente os números", null=True, blank=True)
    cidade_titulo = models.CharField(max_length=20, verbose_name='Cidade onde foi emitido o Titulo', null=True, blank=True)
    num_habilitacao = models.CharField(max_length=50, verbose_name='Número Habilitação', null=True, blank=True)
    cat_habilitacao = models.CharField(max_length=5, verbose_name='Categoria da Habilitação', null=True, blank=True)
    uf_habilitacao = models.CharField(max_length=2, choices=UF, verbose_name='UF. Habilitação', null=True, blank=True)
    dt_primeira_habilitacao = models.DateField(verbose_name="Data da Primeira Habilitação", help_text="Somente os números", null=True, blank=True)
    dt_validade_habilitacao = models.DateField(verbose_name="Data de Validade da Habilitação", help_text="Somente os números", null=True, blank=True)
    dt_primeiro_emprego = models.DateField(verbose_name="Data de Inicio Primeiro Emprego", help_text="Somente os números", null=True, blank=True)
    dt_final_emprego = models.DateField(verbose_name="Data Final do Primeiro Emprego", help_text="Somente os números", null=True, blank=True)
    nome_empresa = models.CharField(max_length=250, verbose_name='Nome da Empresa', null=True, blank=True)
    tipo_sanguineo = models.CharField(max_length=10, verbose_name='Tipos Sanguineo', null=True, blank=True)
    fator_rh = models.CharField(max_length=10, verbose_name='Fator RH', null=True, blank=True)
    num_rne = models.CharField(max_length=15, verbose_name='Número RNE', null=True, blank=True)
    emissor_rne = models.CharField(max_length=15, verbose_name='Emissor RNE', null=True, blank=True)
    dt_emissao_rne = models.DateField(verbose_name="Data de Expedição RNE", help_text="Somente os números", null=True, blank=True)
    clas_trabalho = models.CharField(max_length=10, verbose_name='Classe Trabalho Estrangeiro', null=True, blank=True)
    ctps_n = models.CharField(max_length=10, verbose_name='CTPS:', null=True, blank=True)
    serie_ctps = models.CharField(max_length=15, verbose_name='Serie CTPS', null=True, blank=True)
    estado_ctps = models.CharField(max_length=15, choices=UF, verbose_name='Estato CTPS', null=True, blank=True)
    dt_emissao_ctps = models.DateField(verbose_name="Data de Emissão CTPS", help_text="Somente os números", null=True, blank=True)
    matricula = models.CharField(max_length=20, verbose_name='Matricula Servidor(a)')
    dt_admissao = models.DateField(verbose_name="Data de Admissão", help_text="Somente os números", null=True, blank=True)
    dt_desligamento = models.DateField(verbose_name="Data de Desligamento", help_text="Somente os números", null=True, blank=True)
    dt_posse = models.DateField(verbose_name="Data de Posse", help_text="Somente os números", null=True, blank=True)
    portador_pne = models.CharField(max_length=4, choices=TIPO, verbose_name='Portador de Necessidade Especiais PNE?', null=True, blank=True)
    cargo = models.CharField(max_length=20, verbose_name='Cargo', null=True, blank=True)
    tipo_cargo = models.CharField(max_length=15, choices=TIPO_CARGO, verbose_name='Tipo de Cargo', null=True, blank=True)
    funcao = models.CharField(max_length=150, verbose_name='Função', null=True, blank=True)
    especialidade = models.CharField(max_length=150, verbose_name='Especialidade ', null=True, blank=True)
    relacao_trabalho = models.CharField(max_length=50, choices=RELACAO_TRABALHO, verbose_name='Relação de trabalho', null=True, blank=True)
    regime_trabalho = models.CharField(max_length=50, choices=REGIME_TRABALHO, verbose_name='Regime de Trabalho', null=True, blank=True)
    tipo_vinculo = models.CharField(max_length=50, choices=TIPO_VINCULO, verbose_name='Tipo de Vinculo', null=True, blank=True)
    nivel_salario = models.CharField(max_length=20, verbose_name='Nivel Salarial', null=True, blank=True)
    carga_horaria = models.CharField(max_length=20, verbose_name='Carga Horária', null=True, blank=True)
    banco = models.CharField(max_length=50, verbose_name='Banco', null=True, blank=True)
    agencia = models.CharField(max_length=50, verbose_name='Agencia', null=True, blank=True)
    conta = models.CharField(max_length=50, verbose_name='Conta', null=True, blank=True)

    def __str__(self):
        return self.nome



























