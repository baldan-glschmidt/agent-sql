# R000ASS

## Descrição

Assinalamentos Diversos

---

## Resumo

- Campos: 212
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TamCad | Number(002,0) | Sim | Tamanho do Cadastro do Colaborador |
| EdiCad | String(012) | Sim | Edição do Cadastro do Colaborador |
| ChaPro | String(065) | Sim | Nome do Programa a Chamar |
| NumTel | String(020) | Sim | Telefone Empresa Responsável |
| PesRes | String(030) | Sim | Nome Pessoa Responsável |
| RamRes | String(015) | Sim | Ramal Pessoa Responsável |
| ConMtp | String(010) | Sim | Código Convênio MTPS |
| LitSin | String(013) | Sim | Literal Empregados Singular |
| LitPlu | String(013) | Sim | Literal Empregados Plural |
| MoeSin | String(015) | Sim | Literal Moeda Singular |
| MoePlu | String(015) | Sim | Literal Moeda Plural |
| HorCen | String(001) | Sim | Horas Centesimal |
| UsaAss | String(001) | Sim | Usar Assiduidade |
| UsaQua | String(001) | Sim | Consulta Quadro Lotação |
| TipEmp | String(001) | Sim | Empresa Agência Empregos |
| VerQua | String(001) | Sim | Ver Quadro Transferências |
| UsaTur | String(001) | Sim | Usa Turno QL |
| CodFer | Number(004,0) | Sim | Tabela de Feriados Default p/ Geração Automática da ITRD |
| DatGrr | Date | Sim | Data de Início da GRR |
| RecDes | String(001) | Sim | Recalcular % Desempenho nas Alterações de Salário |
| UsaTov | String(001) | Sim | Usa Turn Over nas Transferências (S,N) |
| EmpAux | String(001) | Sim | Empresa Ativa no Auxílio Educação |
| CtlQua | Number(001,0) | Sim | Tipo de Controle do Quadro de Lotação |
| TipArr | String(001) | Sim | Tipo de Arredondamento de Salários |
| CasHor | Number(001,0) | Sim | Número de Casas Decimais do Salário dos Horistas e dos Tarefeiros |
| JunBas | Number(001,0) | Sim | IR Outro Contrato / Terceiro |
| TimAdm | Number(001,0) | Sim | Verifica Inclusão de Histórico de Time na Admissão |
| RecExt | String(001) | Sim | Ex-Terceiro Recontratado como Terceiro |
| RecEmp | String(001) | Sim | Ex-Terceiro Recontratado como Empregado |
| RecTem | String(001) | Sim | Ex-Empregado Temporário |
| RecInd | String(001) | Sim | Ex-Empregado Indeterminado |
| RecDet | String(001) | Sim | Ex-Empregado Prazo Determinado CLT/safra |
| RecDel | String(001) | Sim | Ex-Empregado Prazo Determinado Lei 9.601/98 |
| RecEst | String(001) | Sim | Estatutários |
| QtdExt | Number(003,0) | Sim | Quantidade de Dias ou Meses |
| QtdEmp | Number(003,0) | Sim | Quantidade de Dias ou Meses |
| QtdTem | Number(003,0) | Sim | Quantidade de Dias ou Meses |
| QtdInd | Number(003,0) | Sim | Quantidade de Dias ou Meses |
| QtdDet | Number(003,0) | Sim | Quantidade de Dias ou Meses |
| QtdDel | Number(003,0) | Sim | Quantidade de Dias ou Meses |
| QtdEst | Number(003,0) | Sim | Quantidade de Dias ou Meses |
| RgrFer | Number(003,0) | Sim | Regra Cálculo Direito Férias |
| RgrLic | Number(003,0) | Sim | Regra Licença Especial |
| RgrApo | Number(003,0) | Sim | Regra Aposentadoria |
| VerQuF | String(001) | Sim | Ver Quadro de Funções nas  Transferências |
| RgrIns | Number(003,0) | Sim | Regra Inserir Afastamento |
| RgrExc | Number(003,0) | Sim | Regra Excluir Afastamento |
| RgrAlt | Number(003,0) | Sim | Regra Alterar Afastamento |
| CriHsa | Number(001,0) | Sim | Cria Histórico Salarial na Troca de Cargo / Posto |
| CriHna | Number(001,0) | Sim | Cria Histórico Natureza de Despesa na Troca de Cargo |
| CriIns | Number(001,0) | Sim | Critica Grau Instrução na Transferência de Cargo / Posto |
| ConCpf | String(001) | Sim | Consistir Colaboradores com Mesmo CPF/PIS |
| UsaRea | String(001) | Sim | Usa Rotina de Readmissão |
| PltPad | Number(005,0) | Sim | Código do Site Padrão da Empresa. |
| AfaIns | Number(001,0) | Sim | Afastamentos INSS Mensalista |
| LotUsu | String(001) | Sim | Controlar Lotes por Usuário |
| TipQua | String(001) | Sim | Tipo de Quadro (Competência/Diário) |
| ConCar | String(001) | Sim | Permite cargos não previstos, na previsão do quadro |
| UltPre | Number(001,0) | Sim | Apresenta coluna Dezembro do ano anterior na coleta (WEB) |
| SalDes | String(001) | Sim | Define sobre qual salário deve ser calculado o % Desempenho |
| NivQua | Number(001,0) | Sim | Nível da estrutura de lotação para controle de cargos previstos |
| AtuEfe | String(001) | Sim | Indica se o Sistema deve atualizar o efetivo do Quadro de Lotação |
| EscDup | String(001) | Sim | Inclusão de Escalas Duplicadas |
| HorDup | String(001) | Sim | Inclusão de Horários Duplicados |
| QtdCTr | Number(002,0) | Sim | Qtde de Colaboradores por Transação no Cálculo |
| MosPPP | String(001) | Sim | Mostra PPP Quando Integrado Com o Módulo Segurança |
| EstRem | String(001) | Sim | Define se controla estoque de medicamento |
| UsaLog | String(001) | Sim | Usa Log Integração Financeira |
| TrfAfa | String(001) | Sim | Transfere Colaboradores Afastados |
| AtuIns | String(001) | Sim | Ao cadastrar histórico de curso, verifica se deve atualizar grau de instrução |
| SalNeg | String(001) | Sim | Define se permite saldo negativo de medicamento |
| AdmRes | Number(001,0) | Sim | Administra reserva de curso (1-Por Participante - 2-Agrupada por competência) |
| PerExc | String(001) | Sim | Considera Períodos de Exceção no Cálculo |
| MsgNov | String(001) | Sim | Indica se deve mostrar mensagem p/ ler o Novidades ao entrar no sistema |
| IndCar | String(001) | Sim | Permite informar cargo diferenciado para ocupação de vaga |
| ReqCar | String(001) | Sim | Verifica requisitos do cargo quando não há bloco informado na exceção |
| TrfEmp | Number(001,0) | Sim | Gera pendências nas transferências de empresa |
| TrfFil | Number(001,0) | Sim | Gera pendências nas transferências de filial |
| TrfLoc | Number(001,0) | Sim | Gera pendências nas transferências de local |
| TrfCcu | Number(001,0) | Sim | Gera pendências nas transferências de centro de custo |
| TrfCar | Number(001,0) | Sim | Gera pendências nas transferências de cargo |
| TrfEsc | Number(001,0) | Sim | Gera pendências nas transferências de Escala |
| DesCol | Number(001,0) | Sim | Gera pendências no desligamento do colaborador |
| DemRes | String(001) | Sim | Retira dos Cadastros de Terceiros o Colaborador Responsável Demitido |
| RquHab | String(001) | Sim | No cadastro de requisitos por local/cargo permite diversos blocos |
| AtuEma | String(250) | Sim | E-Mail do Resp. Pela Atualização dos Históricos |
| CraMar | String(001) | Sim | Verifica Marcações Acesso Baixa/Exclusão Crachás |
| ConPag | String(001) | Sim | Controla pagamento da sentença |
| ColAce | String(001) | Sim | Permite cadastro de colaborador sistema Acesso quando integrado |
| ValPrp | Number(002,0) | Sim | Dias Aviso Validade  Cópia |
| CarHis | String(001) | Sim | Permite descrição histórica dos itens de cargo |
| SReCon | String(001) | Sim | Indica que somente o responsável conclui a avaliação de eficácia |
| CarDCa | String(001) | Sim | Indica que um cargo está disponível em mais de uma carreira |
| LocChe | Number(001,0) | Sim | Indica o nível em que se encontra a chefia |
| LocCol | Number(001,0) | Sim | Indica local do colaborador em rotinas de busca de chefia |
| MonSal | String(001) | Sim | Indica se monitora a tabela de histórico salarial |
| PrvCtb | Number(001,0) | Sim | Definir quais rotinas de provisão e contabilização serão utilizadas |
| AltPer | String(001) | Sim | Só Administrador Altera Permissões Folha\Marcações |
| ConNex | String(001) | Sim | Indica se Controla Nexo Epidemiológico |
| LeiCad | String(001) | Sim | Leitura de Arquivos por Cadastro |
| TipLCa | Number(001,0) | Sim | Tipo Colaborador para Leitura |
| ArqCpD | String(001) | Sim | Considerar Arquivo do Captura Ponto Portaria 373 do Dia Atual na Leitura |
| ConAce | Number(001,0) | Sim | Considerar Acertos |
| ConHvi | String(001) | Sim | Permitir Mesmo Vínculo |
| ConHca | String(001) | Sim | Permitir Mesmo Cargo |
| ConHes | String(001) | Sim | Permitir Mesma Escala |
| EmaPrp | String(250) | Sim | E-mail para Aviso Validade da Proprietária |
| EnvCol | String(001) | Sim | Filtrar Eventos Envelope |
| MonCal | String(001) | Sim | Monitorar Cálculo Folha |
| UsaEqv | String(001) | Sim | Usa Equivalência Específica por Rotina |
| ReqCon | Number(001,0) | Sim | Verificar quais requisitos para gerar avaliação de conhecimento. |
| AdiLoc | String(001) | Sim | Abrir Adicionais por Local ao Inserir Local |
| HabPes | String(001) | Sim | Habilita a rotina de pessoas |
| VinPes | Number(001,0) | Sim | Define a obrigatoriedade do vínculo entre colaborador e pessoa |
| ViPeDe | Number(001,0) | Sim | Define a obrigatoriedade do vínculo entre dependente e pessoa |
| ViPeCa | Number(001,0) | Sim | Define a obrigatoriedade do vínculo entre candidato e pessoa |
| CepAut | String(001) | Sim | Define se o endereço do colaborador será sempre substituído pelo cep informado na ficha complementar |
| EdiPrm | String(005) | Sim | Edição do Cadastro da Permissão |
| EdiRlg | String(005) | Sim | Edição do Cadastro do Coletor |
| CadUni | String(001) | Sim | Número de Cadastro Único Entre Empresas |
| CcuHie | String(001) | Sim | Centro de Custo Hierárquico |
| UsaPos | String(001) | Sim | Habilita a utilização da Estrutura de Postos de trabalho no sistema |
| TapDef | Number(003,0) | Sim | Define o Tipo de atuação padrão para os históricos dos Colaboradores sem Posto |
| MotDef | Number(003,0) | Sim | Define o Mot. de alteração padrão para os históricos dos Colaboradores sem Posto |
| DdiTel | Number(003,0) | Sim | Código DDI |
| DddTel | Number(003,0) | Sim | Código DDD |
| ConPor | Number(001,0) | Sim | Controle da Portaria 1510 |
| InsCua | Number(001,0) | Sim | Define se os instrutores serão colaboradores ou pessoas |
| AltCor | String(001) | Sim | Alternar Cores da Grid |
| CorPar | String(010) | Sim | Cor da Linha Par da Grid |
| CorImp | String(010) | Sim | Cor da Linha Ímpar da Grid |
| TrgInv | String(001) | Sim | Bloquear acesso ao sistema quando identificar triggers inválidas |
| EmaTrg | String(250) | Sim | Informar e-mail do adm. da Base de Dados para aviso de triggers inválidas |
| BlqTrg | String(001) | Sim | Verificação de Triggers inválidas em todas as tabelas ou somente tabelas de históricos. |
| UsaEst | String(001) | Sim | Habilita a utilização das Estruturas no sistema |
| CufDef | Number(004,0) | Sim | Define o padrão para permitir informar nos históricos cursos não tabulados |
| CuaDef | Number(009,0) | Sim | Define o padrão para permitir informar nos históricos cursos não tabulados |
| EntDef | Number(008,0) | Sim | Define o padrão para permitir informar nos históricos entidades não tabuladas |
| VrsRSe | Number(001,0) | Sim | Define qual é a versão do RS que será utilizada |
| AdmCur | Number(001,0) | Sim | Define se os cursos serão tratados por colaboradores ou pessoas |
| PapCar | String(9000) | Sim | Papel de carta padrão usado no envio de e-mail do RS |
| RotGPC | Number(001,0) | Sim | Permite configurar a ativação da rotina de Gestão por competências |
| CodPlt | Number(005,0) | Sim | Código do Site para Marcações do Captura Ponto Portaria 373 |
| CodRlg | Number(005,0) | Sim | Código do Coletor para Marcações do Captura Ponto Portaria 373 |
| AdmEvn | Number(001,0) | Sim | Permite configurar a ativação da rotina de administração de eventos |
| PsqPes | String(001) | Sim | Exibir a tela de pesquisa de pessoas automaticamente ao incluir colaborador |
| ConCur | Number(001,0) | Sim | Permite configurar a forma de sincronização de cursos quando houver conflito |
| UtlMaS | String(001) | Sim | Matrícula Alfanumérica Plano Saúde |
| HabLQL | String(001) | Sim | Habilita o legado de controle do quadro de vagas |
| UsaCVP | String(001) | Sim | Habilita a utilização do controle de vagas por posto de trabalho |
| LeiAFD | Number(001,0) | Sim | Leitura do Arquivo de Marcações AFD |
| ComPos | String(100) | Sim | Composição do código do posto de trabalho para propostas de alteração do quadro |
| RodMod | Number(001,0) | Sim | Empresa apresentada no Rodapé dos modelos |
| AtuAbr | String(001) | Sim | Atualiza abrangência dinamica automaticamente em ambiente middleware |
| AfaFle | Number(001,0) | Sim | Definir apuração de Horário Tipo 3-Flexível com Afastamento |
| EdiPlt | String(005) | Sim | Edição do Cadastro do Site |
| DatMot | Date | Sim | Data de Inicio da Lei 13.103 dos Motoristas |
| MobPlt | Number(005,0) | Sim | Site para Marcações do Mobilidade |
| MobRlg | Number(005,0) | Sim | Coletor para Marcações do Mobilidade |
| PosSeg | String(001) | Sim | Habilita a utilização da Estrutura de Postos de trabalho (Acesso) |
| NovLoc | String(001) | Sim | Nova Estrutura Locais - PosLoc com 2 ou 3 caracteres |
| AltCaP | Number(001,0) | Sim | Alteração nas Características do Posto Trabalho |
| TranBH | String(001) | Sim | Tratar banco de horas na transferência de filial |
| ManHRR | Number(001,0) | Sim | Manter Histórico das Reservas de Vagas das Requisições |
| MarGer | String(001) | Sim | Exibir confirmação ao apurar após excluir marcações geradas |
| IntSAM | String(001) | Sim | Integra com o Ronda Senior X |
| ConSis | Number(001,0) | Sim | Considerar Base Fora do Sistema |
| BusCal | Number(001,0) | Sim | Buscar Base de Cálculo |
| IntVis | String(001) | Sim | Integra Visitante com o Ronda Senior X |
| IntAlu | String(001) | Sim | Integra Aluno com o Ronda Senior X |
| IntRes | String(001) | Sim | Integra Responsável Aluno com o Ronda Senior X |
| IntPac | String(001) | Sim | Integra Paciente com o Ronda Senior X |
| IntAce | String(001) | Sim | Integra Marcação de Acesso com o Ronda Senior X |
| IntAlm | String(001) | Sim | Integra Alarme e Notificação de Dispositivo com o Ronda Senior X |
| FilEmp | String(001) | Sim | Utiliza Empresas Cadastradas Como Filiais |
| IntPlf | String(001) | Sim | Integra Local Físico com o Ronda Senior X |
| IntDsp | String(001) | Sim | Integra Dispositivo com o Ronda Senior X |
| SenInt | String(030) | Sim | Senha Ativação Intermitente |
| SenRec | String(030) | Sim | Senha Ativação Para Informar Recibo Manual no eSocial |
| SenASe | String(030) | Sim | Senha Ativação Para a Simplificação eSocial |
| IntUsu | String(001) | Sim | Integra Usuário Associado a Colaborador com o Ronda Senior X |
| IntFot | String(001) | Sim | Integra fotos de pessoas com o Ronda Senior X |
| IntTvi | String(001) | Sim | Integra tipo de visita com o Ronda Senior X |
| CepWeb | String(001) | Sim | Buscar dados do CEP via WebService quando ainda não conter na base local |
| IntEmp | String(001) | Sim | Integra empresa com o Ronda Senior X |
| IntFil | String(001) | Sim | Integra filial com o Ronda Senior X |
| IntCar | String(001) | Sim | Integra cargo com o Ronda Senior X |
| IntCCu | String(001) | Sim | Integra centro de custo com o Ronda Senior X |
| IntOrg | String(001) | Sim | Integra organograma com o Ronda Senior X |
| IntCon | String(001) | Sim | Integra outra empresa/contrato com o Ronda Senior X |
| FinRes | Number(001,0) | Sim | Ficha Financeira Rescisão |
| ConInt | Number(001,0) | Sim | Cálculo Intermitente |
| AtuSit | Number(001,0) | Sim | Atualizar Situação do Cálculo |
| PerUso | String(001) | Sim | Permitir campos de usuários em Históricos durante o cadastro de novo colaborador |
| IntPrm | String(001) | Sim | Integra permissão com o Ronda Senior X |
| IntEsc | String(001) | Sim | Integra escala do colaborador com o Ronda Senior X |
| ValCir | Number(001,0) | Sim | Validação circular base de eventos |
| SenLim | String(030) | Sim | Senha Ativação Liminar Terceiros |
| SenRPA | String(030) | Sim | Senha Ativação Liminar RPA de Terceiros |
| SenEsf | String(030) | Sim | Senha Ativação Envio Layouts eSfinge |
| DesEso | String(001) | Sim | Descrição de Jornada eSocial Simplificada no Histórico de Escala/Horário |
| IntGTE | String(001) | Sim | Integra com o Gestão de Terceiros/Ronda Senior X |
| IntVld | String(001) | Sim | Integra Validades da Pessoa ASO/Treinamento com o Ronda Senior X |
| IntPrc | String(001) | Sim | Integra eventos S-2500 e/ou S-2501 pelo cadastro da Ação |
| TraBSi | String(001) | Sim | Tratar banco de horas na transferência de sindicato |
| CanEfe | String(001) | Sim | Motivo do Cancelamento de Efetivação do Candidato |
| CnvAct | String(001) | Sim | Usa Conversão Lic. Saúde (FGTS Dig.) |
| FraCpf | Number(005,0) | Sim | Quantidade de CPFs para fracionamento na geração do leiaute eSocial S-2501 |
| CnvAlf | Number(001,0) | Sim | Habilita conversor do CNPJ alfanumérico |
| GeHCus | String(001) | Sim | Utilizar Legendas Customizadas no Gerenciar Horários no Gestão do Ponto |
| CfjAlf | String(001) | Sim | Permite informar alfanumérico no Cnpj |
| VerDia | String(001) | Sim | Habilita a execução de regra na verificação do dia |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R000ASS_122

**Tabela:** R017TAP

| Origem | Destino |
|--------|---------|
| TapDef | CodTap |

### IR_R000ASS_123

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| MotDef | CodMot |

