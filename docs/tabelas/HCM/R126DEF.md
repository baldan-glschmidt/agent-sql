# R126DEF

## Descrição

Requisitos - Definições para Seleção

---

## Resumo

- Campos: 178
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DefPes | String(001) | Sim | Definição para Peso |
| DefAlt | String(001) | Sim | Definição para Altura |
| DefIda | String(001) | Sim | Definição para Idade |
| DefSex | String(001) | Sim | Definição para Sexo |
| DefVei | String(001) | Sim | Definição para Veículo |
| DefCiv | String(001) | Sim | Definição para Estado Civil |
| DefSlc | String(001) | Sim | Definição para Solicitação |
| DefNac | String(001) | Sim | Definição para Nacionalidade |
| DefIns | String(001) | Sim | Definição para Grau de Instrução |
| DefQua | String(001) | Sim | Definição para Qualificação |
| DefTre | String(001) | Sim | Definição para Tipo Referência Pessoal |
| DefRlr | String(001) | Sim | Definição para Religião |
| DefCfo | String(001) | Sim | Definição para Curso Formação |
| DefCap | String(001) | Sim | Definição para Curso Aperfeiçoamento |
| DefCnc | String(001) | Sim | Definição para Conhecimento |
| DefEfo | String(001) | Sim | Definição para Entidade do Curso de Formação |
| DefEap | String(001) | Sim | Definição para Entidade do Curso de Aperfeiçoamento |
| DefTur | String(001) | Sim | Definição para Turno |
| DefHor | String(001) | Sim | Definição para Horário |
| DefCid | String(001) | Sim | Definição para Cidade |
| DefBai | String(001) | Sim | Definição para Bairro |
| DefRfo | String(001) | Sim | Definição para Fonte Recrutamento |
| DefPsl | String(001) | Sim | Definição para Parecer de Selecionador |
| DefPps | String(001) | Sim | Definição para Parecer Psicólogo |
| DefPsu | String(001) | Sim | Definição para Parecer Superior |
| DefEta | String(001) | Sim | Definição para Etapas |
| DefIta | String(001) | Sim | Definição para Avaliação |
| DefItq | String(001) | Sim | Definição para Questionário |
| DefExa | String(001) | Sim | Definição para Exame Médico |
| DefCar | String(001) | Sim | Definição para Cargo |
| DefLoc | String(001) | Sim | Definição para Local |
| DefEqc | String(001) | Sim | Definição para Equivalência de Cargo |
| DefEqe | String(001) | Sim | Definição para Equivalência de Experiência |
| DefSal | String(001) | Sim | Definição para Salário |
| DefPrf | String(001) | Sim | Definição para Conselho Profissional |
| DefFil | String(001) | Sim | Definição para Filial |
| RgeIni | Number(003,0) | Sim | Código da Regra para Inicialização da Efetivação |
| RgeAnt | Number(003,0) | Sim | Código da Regra Antes Efetivar Candidato |
| RgeDep | Number(003,0) | Sim | Código da Regra Depois Efetivar Candidato |
| RgeFin | Number(003,0) | Sim | Código da Regra para Finalização da Efetivação |
| RgtIni | Number(003,0) | Sim | Código da Regra para Inicialização da Triagem |
| RgtFin | Number(003,0) | Sim | Código da Regra para Finalização da Triagem |
| ModCol | String(011) | Sim | Modelo Gerador Relatórios 1º Botão - Colaborador - Triagem/Seletiva |
| ModCan | String(011) | Sim | Modelo Gerador Relatórios 1º Botão - Candidato - Triagem/Seletiva |
| EfeFic | Number(001,0) | Sim | Tipo Código Ficha para Efetivação |
| RgdIni | Number(003,0) | Sim | Código da Regra para Inicialização Atualização |
| RgdAnt | Number(003,0) | Sim | Código da Regra Antes Atualização Candidato |
| RgdDep | Number(003,0) | Sim | Código da Regra Depois Atualização Candidato |
| RgdFin | Number(003,0) | Sim | Código da Regra para Finalização Atualização |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos Default |
| CodCar | String(024) | Sim | Cargo Default (Empregos Anteriores) |
| OemDef | Number(008,0) | Sim | Outra Empresa Default (Empregos Anteriores) |
| RegFic | Number(003,0) | Sim | Código da Regra para Gerar Ficha Médica |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| CanRef | String(001) | Sim | Cancelar Requisições com Efetivações |
| GraInP | Number(002,0) | Sim | Grau de Instrução Pai |
| GraInM | Number(002,0) | Sim | Grau de Instrução Mãe |
| GraInC | Number(002,0) | Sim | Grau de Instrução Cônjuge |
| EstCiP | Number(001,0) | Sim | Estado Civil Pai |
| EstCiM | Number(001,0) | Sim | Estado Civil Mãe |
| EstCiC | Number(001,0) | Sim | Estado Civil Cônjuge |
| AbrPar | String(050) | Sim | Abrangência de Parecer Médico Aceitável para ASO |
| DefAso | String(001) | Sim | Definição para ASO |
| DefDef | String(001) | Sim | Definição para Deficiência |
| UsaCon | String(001) | Sim | Utiliza concurso público |
| DetEli | String(001) | Sim | Detalha eliminação do candidato |
| DefCnh | String(001) | Sim | Definição para Categoria Habilitação |
| DefEst | String(001) | Sim | Definição para Estado |
| AbrCol | String(009) | Sim | Abrangência Tipo Colaborador |
| NomCan | String(001) | Sim | Consiste o cadastro de candidato pelo nome |
| DefMap | String(001) | Sim | Definição para Resultado do MAP |
| NomBo1 | String(015) | Sim | Nome do botão que será disponibilizado na tela de concurso |
| NomBo2 | String(015) | Sim | Nome do botão que será disponibilizado na tela de concurso |
| NomBo3 | String(015) | Sim | Nome do botão que será disponibilizado na tela de concurso |
| NomBo4 | String(015) | Sim | Nome do botão que será disponibilizado na tela de concurso |
| NomBo5 | String(015) | Sim | Nome do botão que será disponibilizado na tela de concurso |
| NomBo6 | String(015) | Sim | Nome do botão que será disponibilizado na tela de concurso |
| NomBo7 | String(015) | Sim | Nome do botão que será disponibilizado na tela de concurso |
| NomBo8 | String(015) | Sim | Nome do botão que será disponibilizado na tela de concurso |
| RepEta | String(001) | Sim | Permitir a mesma etapa no mesmo processo |
| DefPch | String(001) | Sim | Definição para palavras-chave |
| DefAre | String(001) | Sim | Definição para área de atuação |
| DefHie | String(001) | Sim | Definição para hierarquia do cargo |
| EmpEla | String(010) | Sim | Identificação do cliente para a Elancers |
| NomBoA | String(020) | Sim | Nome do 1º Botão - tratamento candidato externo |
| NomBoB | String(020) | Sim | Nome do 2º Botão - tratamento candidato externo |
| ModBoA | String(011) | Sim | Modelo Gerador Relatórios 1º Botão - tratamento candidato externo |
| ModBoB | String(011) | Sim | Modelo Gerador Relatórios do 2º Botão - tratamento candidato externo |
| CodRgA | Number(003,0) | Sim | Código da regra do 1º Botão - tratamento candidato externo |
| CodRgB | Number(003,0) | Sim | Código da regra do 2º Botão - tratamento candidato externo |
| AprAva | String(001) | Sim | Disponibiliza recurso para aprovação de avaliação de candidato |
| CtlVag | String(001) | Sim | Limita vagas por área, conforme vagas do cargo do concurso |
| NomBIA | String(020) | Sim | Nome do 1º Botão - tratamento candidato interno |
| NomBIB | String(020) | Sim | Nome do 2º Botão - tratamento candidato interno |
| ModBIA | String(011) | Sim | Modelo Gerador Relatórios 1º Botão - tratamento candidato interno |
| ModBIB | String(011) | Sim | Modelo Gerador Relatórios 2º Botão - tratamento candidato interno |
| CodRIA | Number(003,0) | Sim | Código da regra do 1º Botão - tratamento candidato interno |
| CodRIB | Number(003,0) | Sim | Código da regra do 2º Botão - tratamento candidato interno |
| NomBI1 | String(020) | Sim | Nome do 1º Botão Triagem/Seletiva |
| NomBI2 | String(020) | Sim | Nome do 2º Botão Triagem/Seletiva |
| ModCo2 | String(011) | Sim | Modelo Gerador Relatórios 2º Botão - Colaborador - Triagem/Seletiva |
| ModCa2 | String(011) | Sim | Modelo Gerador Relatórios 2º Botão - Candidato - Triagem/Seletiva |
| AtuDad | String(001) | Sim | Indica se deve atualizar a grid de candidatos |
| OutReq | String(001) | Sim | Identificar os candidatos que participam de outras requisições (Triagem/Seletiva) |
| AbrSit | String(020) | Sim | Situações que podem ser consideradas ao relacionar um candidato à requisição |
| DefEqf | String(001) | Sim | Definição para Equivalência do Curso de Formação |
| DefEqa | String(001) | Sim | Definição para Equivalência do Curso de Aperfeiçoamento |
| MsgCon | String(001) | Sim | Apresentar mensagem quando a rotina de concurso público está habilitada |
| AbrAso | String(050) | Sim | Abrangência de Tipo de ASO |
| UsaDep | String(001) | Sim | Usa dependentes de candidatos externos |
| NomRq1 | String(020) | Sim | Nome do Botão - Cadastro da Requisição |
| ModRq1 | String(011) | Sim | Modelo Gerador Relatórios - Cadastro da Requisição |
| CodRq1 | Number(003,0) | Sim | Código da Regra - Cadastro da Requisição |
| CodRl1 | Number(003,0) | Sim | Código da regra do 1º Botão - Triagem/Seletiva |
| CodRl2 | Number(003,0) | Sim | Código da regra do 2º Botão - Triagem/Seletiva |
| FimEta | String(001) | Sim | Exigir data final na definição das etapas da requisição |
| HisEli | String(001) | Sim | Mantém histórico de eliminação dos candidatos com interesse na vaga |
| DefTxv | String(001) | Sim | Definição para palavra-chave no texto do currículo |
| HabCvf | String(001) | Sim | Habilitar Currículo Formatado |
| RegSen | Number(003,0) | Sim | Código da Regra - Enviar nova senha para o candidato |
| EmaPad | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) do Remetente Padrão |
| ModCur | String(011) | Sim | Modelo de relatórios do currículo do candidato externo |
| AbrTip | String(050) | Sim | Abrangência de tipo de requisição que será considerada no gerenciamento do processo seletivo na WEB |
| ModInt | String(011) | Sim | Modelo de relatórios do currículo do candidato interno |
| NomBCu | String(020) | Sim | Configura a descrição do botão que apresenta o Currículo |
| ModBCu | String(011) | Sim | Define o modelo que apresenta o Currículo do candidato externo |
| ModBCo | String(011) | Sim | Define o modelo que apresenta o Currículo do candidato interno |
| RquSim | Number(001,0) | Sim | Tipo de verificação para Candidatos em Processos Seletivos simultâneos |
| ModBCa | String(011) | Sim | Define o modelo que é apresentado na tela de candidaturas por anúncio. |
| ThpSub | Number(003,0) | Sim | Tipo de Hierarquia do Posto de trabalho para substituição |
| ThpAum | Number(003,0) | Sim | Tipo de Hierarquia do Posto de trabalho para aumento de vaga |
| MotSal | Number(003,0) | Sim | Motivo de alteração salarial padrão |
| AbrPrf | String(100) | Sim | Indica as utilizações de grupo de requisitos consideradas no recrutamento |
| OriReq | Number(001,0) | Sim | Origem dos Requisitos das Requisições |
| AutOEM | Number(001,0) | Sim | Carregar autocompletar de Outras empresas |
| AutCAR | Number(001,0) | Sim | Carregar autocompletar de Cargos |
| AutCUF | Number(001,0) | Sim | Carregar autocompletar de Cursos de Formação |
| AutCUA | Number(001,0) | Sim | Carregar autocompletar de Cursos de Aperfeiçoamento |
| AutPAI | Number(001,0) | Sim | Carregar autocompletar de Países |
| AutEST | Number(001,0) | Sim | Carregar autocompletar de Estados |
| AutCID | Number(001,0) | Sim | Carregar autocompletar de Cidades |
| CarAut | Number(001,0) | Sim | Número mínimo de caracteres digitados para ativar o autocompletar |
| TemAut | Number(004,0) | Sim | Tempo (ms) após o último caractere ser teclado para ativar o autocompletar |
| LimAut | Number(003,0) | Sim | Limite de registros retornados em campos autocompletar |
| RecTra | Number(001,0) | Sim | Verifica ao cadastrar um candidato se o mesmo possui reclamação trabalhista |
| CepAut | Number(001,0) | Sim | Define se ao informar o CEP no Currículo Web deve sugerir o respectivo endereço |
| ConExp | Number(001,0) | Sim | Define se utilizará controle de expiração da sessão no Currículo Web |
| EstCpr | Number(004,0) | Sim | Código da Estrutura de Cargos Pretendidos |
| PerBai | String(001) | Sim | Permite informar bairros não cadastrados no cadastro de candidatos |
| DefCom | Number(001,0) | Sim | E-mail de comunicação com o candidato |
| PerPCl | String(001) | Sim | Permite realizar pré-classificação em concurso público |
| GraIns | Number(001,0) | Sim | Define como pesquisar pelo Grau de Instrução |
| AtiDem | String(001) | Sim | Permite configurar a ativação do candidato ao demitir um colaborador |
| PerAtu | String(001) | Sim | Permite informar ramos de atuação não cadastrados previamente |
| PerRad | String(001) | Sim | Permite informar regiões administrativas não cadastradas previamente |
| BotPG1 | String(020) | Sim | Descrição do 1º Botão |
| BotPG2 | String(020) | Sim | Descrição do 2º Botão |
| BotPG3 | String(020) | Sim | Descrição do 3º Botão |
| BotPG4 | String(020) | Sim | Descrição do 4º Botão |
| ModIn1 | String(011) | Sim | Relatório do 1º Botão - Candidatos Internos |
| ModIn2 | String(011) | Sim | Relatório do 2º Botão - Candidatos Internos |
| ModIn3 | String(011) | Sim | Relatório do 3º Botão - Candidatos Internos |
| ModIn4 | String(011) | Sim | Relatório do 4º Botão - Candidatos Internos |
| ModEx1 | String(011) | Sim | Relatório do 1º Botão - Candidatos Externos |
| ModEx2 | String(011) | Sim | Relatório do 2º Botão - Candidatos Externos |
| ModEx3 | String(011) | Sim | Relatório do 3º Botão - Candidatos Externos |
| ModEx4 | String(011) | Sim | Relatório do 4º Botão - Candidatos Externos |
| RegPG1 | Number(003,0) | Sim | Código da Regra do 1º Botão |
| RegPG2 | Number(003,0) | Sim | Código da Regra do 2º Botão |
| RegPG3 | Number(003,0) | Sim | Código da Regra do 3º Botão |
| RegPG4 | Number(003,0) | Sim | Código da Regra do 4º Botão |
| UsoBo1 | Number(001,0) | Sim | Define o uso do 1º Botão (Pesquisa de Candidatos e/ou Gerenciar Processo Seletivo) |
| UsoBo2 | Number(001,0) | Sim | Define o uso do 2º Botão (Pesquisa de Candidatos e/ou Gerenciar Processo Seletivo) |
| UsoBo3 | Number(001,0) | Sim | Define o uso do 3º Botão (Pesquisa de Candidatos e/ou Gerenciar Processo Seletivo) |
| UsoBo4 | Number(001,0) | Sim | Define o uso do 4º Botão (Pesquisa de Candidatos e/ou Gerenciar Processo Seletivo) |
| AceCan | Number(001,0) | Sim | Acesso dos candidatos pendente de aceite de nova versão do termo |
| EfeCan | Number(001,0) | Sim | Permitir efetivar candidatos sem aceite de nova versão do termo |
| CmpAux | Number(001,0) | Sim | Campo auxiliar LGPD |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
