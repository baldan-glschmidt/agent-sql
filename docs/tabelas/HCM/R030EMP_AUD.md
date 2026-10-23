# R030EMP_AUD

## Descrição

Empresas - Auditoria

---

## Resumo

- Campos: 159
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequência Registro |
| VerSeq | Number(010,0) | Não | Versão Sequência |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NomEmp | String(040) | Sim | Razão Social da Empresa |
| ApeEmp | String(040) | Sim | Apelido da Empresa |
| SigEmp | String(005) | Sim | Sigla da Empresa |
| CodPai | Number(004,0) | Sim | Determina qual é o país da empresa |
| NumTel | String(020) | Sim | Número do Telefone da Empresa |
| NumFax | String(015) | Sim | Número do Fax da Empresa |
| CadBom | Number(002,0) | Sim | 0=Ok, 1=Q.Leitura, 2=Q.Virada |
| TotCtb | String(001) | Sim | Totais contabilização (E/F) |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| PerAdi | Number(005,2) | Sim | Perc. adiantamento |
| Med13s | Number(001,0) | Sim | Incluir Médias Adto 13° Salário |
| Cpl13s | String(001) | Sim | Calcular 13° Salário Complementar em Dezembro |
| FecDig | String(001) | Sim | Fechamento Lançamento de Eventos |
| DsrMen | String(001) | Sim | Dsr Mensalistas (S,N) |
| GerAfa | String(001) | Sim | Tipo de Geração de Horas nos Afastamentos dos Horistas |
| EscHor | String(001) | Sim | Usa Escalas de Horário (S,N) |
| UsaVtr | String(001) | Sim | Usa Rotina Transporte |
| UsaDep | String(001) | Sim | Usa Rotina Dependentes |
| UsaVli | String(001) | Sim | Usa Valores Livres |
| FecSal | String(001) | Sim | Fechamento Salários (S,N) |
| UsaRat | String(001) | Sim | Calcular Rateio Mão-de-Obra (N,C,L) |
| RatPrv | String(001) | Sim | Usa Rateio Provisões (S,N) |
| HorNot | String(001) | Sim | Tipo Hora Noturna 52:30 (S,N) |
| PagEsc | String(001) | Sim | Paga carnê no escritório (S,N) |
| GrpSoc | String(001) | Sim | Emite Gps Sócios (S,N) |
| PagAnu | String(001) | Sim | Paga anuidade (N,T,P,M) |
| FecCom | String(001) | Sim | Fechamento digitação compras |
| DiaHor | String(001) | Sim | Gerar dias / horas (D,H) |
| UsaPis | String(001) | Sim | Recolhe % PIS sobre Total da Folha (S,N) |
| CalSal | String(001) | Sim | Salário Hora Mensalistas (M,D) |
| TipUlt | String(001) | Sim | Ultimo Proc. (M,A,S,Q,D) |
| HorFer | String(001) | Sim | Horas no Feriado (A,D) |
| UltPro | Number(005,0) | Sim | Código Últ.Processamento |
| UltMen | Number(005,0) | Sim | Código Últ.Proc.Mensal |
| UltAdt | Number(005,0) | Sim | Código Últ.Proc.Adto. |
| UltSem | Number(005,0) | Sim | Código Últ.Proc.Semanal |
| UltQui | Number(005,0) | Sim | Código Últ.Proc.Quinzenal |
| Ult13s | Number(005,0) | Sim | Código Últ.Proc. 13° Salário |
| UltPar | Number(005,0) | Sim | Código Últ.Proc.Part.Lucros |
| EncPrv | Number(004,2) | Sim | Percentual de Encargos p/ Provisão de Férias e 13° Salário |
| BenPrv | String(001) | Sim | Considerar Incidência Eventos para INSS e FGTS |
| SldPrv | String(001) | Sim | Controlar Saldo Negativo na Provisão de Férias |
| PisPrv | Number(004,2) | Sim | Percentual Provisão PIS |
| BaiRat | String(001) | Sim | Baixa Provisão Rateada (P/F) |
| CtbFer | String(001) | Sim | Forma de Contabilização das Férias |
| CtbEfe | String(001) | Sim | Forma de Contabilização dos Encargos das Férias |
| TotPis | Number(004,0) | Sim | Código do Totalizador do PIS |
| NroCon | Number(007,0) | Sim | Número do contrato Unimed |
| UltRpa | Number(009,0) | Sim | Último RPCI Emitido |
| UsaRah | String(001) | Sim | Usar Rateio Apuração de Horas |
| PorEmp | Number(001,0) | Sim | Porte Empresa (Simples) |
| CmpSim | Date | Sim | Data início Opção Simples |
| SalPrp | String(001) | Sim | Salário Proporcional Quando Houver Reajuste (S,N) |
| UsaTim | String(001) | Sim | Usa Time (S,N) |
| HomPag | String(050) | Sim | Home Page da Empresa |
| HorCtt | String(001) | Sim | Controla Horas Contratuais |
| CtlDfi | String(001) | Sim | Controla Deficientes Físicos (S,N) |
| HisFnc | Number(001,0) | Sim | Histórico Utilizado para Pagamento do Adicional de Função |
| PagFnc | Number(001,0) | Sim | Base para Pagamento do Adicional de Função |
| ProFix | String(001) | Sim | Proporcionalizar Eventos Fixos |
| UsaPrf | String(001) | Sim | Usa Rotina de Professores |
| VacFre | String(001) | Sim | Controla Vacinação/Frequência |
| PrvFer | String(001) | Sim | Provisão de Férias |
| ProAdi | String(001) | Sim | Proporcionalizar Eventos Adicionais |
| OrcMao | String(001) | Sim | Tipo de Orçamento Mão de Obra |
| ConPag | String(001) | Sim | Controla Pagamento |
| CpfRes | Number(011,0) | Sim | CPF Responsável perante o CNPJ da pessoa jurídica |
| ApuPRo | String(001) | Sim | Apura Professor no Ronda |
| CalDpn | String(001) | Sim | Calcula Diferença Positiva/Negativa |
| CodDAp | Number(002,0) | Sim | Código da Definição da Apuração |
| CodDSi | Number(003,0) | Sim | Código da Definição das Situações da Apuração |
| UsaFIn | String(001) | Sim | Usa Rotina de Férias Interrompidas |
| ResDad | String(001) | Sim | Responsável Dados |
| PrvTrf | String(001) | Sim | Baixa Provisão Transferência |
| LanDem | String(001) | Sim | Considerar Lançamentos Demitidos |
| CfgSap | String(100) | Sim | CFG para conexão na base do ERP |
| IntSap | Number(001,0) | Sim | Incluir Empresa na Integração com outro Sistema |
| TabInt | String(001) | Sim | Habilita a geração da tabela R048CON na contabilização |
| FerSab | String(001) | Sim | Feriado Sábado Compensado |
| AtuEfe | String(001) | Sim | Indica se o Sistema deve atualizar o efetivo do Quadro de Lotação |
| VerAdm | String(001) | Sim | Ver Quadro Admissão |
| VerQua | String(001) | Sim | Ver Quadro Transferências |
| VerQuF | String(001) | Sim | Ver Quadro de Funções nas  Transferências |
| UsaTur | String(001) | Sim | Usa Turno QL |
| CtlQua | Number(001,0) | Sim | Tipo de Controle do Quadro de Lotação |
| TipQua | String(001) | Sim | Tipo de Quadro (Competência/Diário) |
| ConCar | String(001) | Sim | Permite cargos não previstos, na previsão do quadro |
| NivQua | Number(001,0) | Sim | Nível da estrutura de lotação para controle de cargos previstos |
| UltPre | Number(001,0) | Sim | Apresenta coluna Dezembro do ano anterior na coleta (WEB) |
| ExcPre | Number(001,0) | Sim | Na manutenção quadro, permite excluir cargo com efetivo |
| AprNat | String(001) | Sim | Na manutenção quadro, apresenta natureza despesa |
| BakIni | Number(009,0) | Sim | Cadastro Inicial Backup |
| BakFim | Number(009,0) | Sim | Cadastro Final Backup |
| ConCFI | String(001) | Sim | Indica se a contabilização utilizará rateio pela conta financeira |
| ConTpv | String(001) | Sim | Controla quadro pelo tipo de vaga(empregado,terceiro,parceiro,etc.) |
| ConTmp | String(001) | Sim | Controla vagas temporárias no quadro de lotação |
| NorRqu | String(001) | Sim | Executado normalização das reservas da requisição |
| SimFil | String(001) | Sim | Permite Opção Simples por Filial |
| AjuSld | Number(001,0) | Sim | Contabilização Saldo Transferido Provisão |
| AprFai | String(001) | Sim | Apresenta coluna Faixa na manutenção do quadro de lotação |
| AprLot | String(001) | Sim | Apresenta coluna Lotados na manutenção do quadro de lotação |
| OrcInd | String(001) | Sim | Define se o cálculo do orçamento será individual(por colaborador) |
| IdaDep | Number(001,0) | Sim | Idade Limite Dependente IR |
| UsaSld | String(001) | Sim | Demonstra Saldo Transferido Provisão (S,N) |
| ConFis | String(001) | Sim | Determinar se devem ser feitos os lançamentos no módulo Fiscal do ERP |
| RotTom | String(001) | Sim | Usa Rotina de Tomadores de Serviço |
| ValCap | Number(014,2) | Sim | Valor capital da empresa |
| TipSij | Number(001,0) | Sim | Indica o tipo SIJP |
| AliRed | String(001) | Sim | Indica se a empresa possui redução de impostos |
| HisCon | String(001) | Sim | Histórico de Contas Bancárias |
| AdmPer | String(015) | Sim | Código da Administradora de Riscos Profissionais |
| CodIdn | Number(015,0) | Sim | Código de identificação da empresa |
| HisPen | String(001) | Sim | Histórico de Pensão Judicial |
| CodDgh | Number(003,0) | Sim | Código da Definição Gerenciar Horários |
| BaiFgt | String(001) | Sim | Baixa Provisão FGTS 13° Salário Adto |
| SelCen | Number(001,0) | Sim | Define a forma de seleção de cenário |
| PasPrv | Number(001,0) | Sim | Determinar Como Será a Contabilização do Passivo da Provisão |
| GerVOC | String(001) | Sim | Define se deve gerar valores calculados no cenário nas tabelas do orçamento coletivo |
| EntCas | String(001) | Sim | Usa Rotina de Casas |
| ClcSai | String(001) | Sim | Identificar Saída/Entrada CLC Trf |
| BaiPis | String(001) | Sim | Baixa Provisão Pis 13° Salário Adto |
| ConSit | String(001) | Sim | Consistir se o Cálculo Está Com Situação "Inicializado" |
| ModInf | String(011) | Sim | Modelo Padrão Ficha Registro - Informações Gerais |
| ModP41 | String(011) | Sim | Modelo Padrão Ficha Registro - Portaria 41 |
| AbrCen | String(001) | Sim | Define como será aplicada a abrangência de usuário no cenário |
| IntDem | Number(001,0) | Sim | Define se considera colaboradores na Integração do BS com Rubi |
| VinPes | Number(001,0) | Sim | Define a obrigatoriedade do vínculo entre empregado e pessoa |
| VinPe2 | Number(001,0) | Sim | Define a obrigatoriedade do vínculo entre terceiro e pessoa |
| VinPe3 | Number(001,0) | Sim | Define a obrigatoriedade do vínculo entre parceiro e pessoa |
| ViPeDe | Number(001,0) | Sim | Define a obrigatoriedade do vínculo entre dependente e pessoa |
| DifImp | String(001) | Sim | Diferença de Impostos |
| UsaPEm | Number(001,0) | Sim | Habilita os Postos de trabalho para os Colaboradores do tipo Empregados |
| UsaPTe | Number(001,0) | Sim | Habilita os Postos de trabalho para os Colaboradores do tipo Terceiros |
| UsaPPa | Number(001,0) | Sim | Habilita os Postos de trabalho para os Colaboradores do tipo Parceiros |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| DddFax | Number(003,0) | Sim | Código DDD do Fax |
| DdiFax | Number(003,0) | Sim | Código DDI do Fax |
| BasIns | String(001) | Sim | Considerar Outros Pagamentos Para Base de INSS no RPCI |
| LimFil | String(001) | Sim | Permite Liminar por Filial |
| UsaCom | String(001) | Sim | Habilita a utilização do controle de compromissos para a empresa |
| BlqAdm | Number(001,0) | Sim | Bloqueia admissões no Adm de Pessoal quando integrado ao Recrutamento e Seleção |
| TabEst | Number(004,0) | Sim | Define qual é a estrutura padrão da empresa |
| NivLoc | Number(002,0) | Sim | Nível de local utilizado para retornar a descrição do local na ficha financeira |
| OrdFRe | Number(001,0) | Sim | Ordenação por data dos históricos da Ficha Registro. |
| ConEmi | Number(001,0) | Sim | Controla emissão de arquivos bancários |
| IniTom | Date | Sim | Data início do uso da rotina de tomadores por rateio |
| ArqIns | String(100) | Sim | Arquivo de instalação (Inst.Ctrl) para conexão na base do ERP |
| AmbSap | String(100) | Sim | Ambiente para conexão na base do ERP |
| RatAdt | Number(001,0) | Sim | Rateio Desconto Adiantamento |
| CenDif | Number(003,2) | Sim | Diferença mínima de valor para recalcular os eventos |
| BusRec | Number(001,0) | Sim | Buscar Receita Desoneração |
| AdiPos | Number(001,0) | Sim | Histórico Posto Adicional |
| UsaHag | String(001) | Sim | Usa Histórico de Vales Gerados |
| DatHag | Date | Sim | Data Início Rotina Histórico de Vales Gerados |
| FToPis | Date | Sim | Fim Uso Totalizador PIS |

---

## Chave Primária

- SeqReg
- VerSeq
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030EMP_AUD_006

**Tabela:** R074PAI

| Origem | Destino |
|--------|---------|
| CodPai | CodPai |

