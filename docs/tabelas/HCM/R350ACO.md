# R350ACO

## Descrição

S-2206 - eSocial - Alteração de Contrato de Trabalho/Relação Estatutária

---

## Resumo

- Campos: 82
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqAco | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de Inscrição do Contribuinte |
| CfjIns | String(014) | Sim | Número de Inscrição do Contribuinte |
| CpfTra | Number(011,0) | Sim | Número do CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado |
| MatTra | String(030) | Sim | Matrícula do Trabalhador |
| DatAlt | Date | Sim | Data de Alteração |
| DatEfe | Date | Sim | Data de Efeito |
| RegTra | Number(001,0) | Sim | Tipo de regime trabalhista |
| RegPre | Number(002,0) | Sim | Tipo de regime previdenciário |
| RegJor | Number(001,0) | Sim | Regime de Jornada do empregado |
| NatAti | Number(001,0) | Sim | Natureza da atividade |
| DatBas | Number(002,0) | Sim | Mês relativo à data base da categoria profissional do trabalhador. |
| SinCat | Number(014,0) | Sim | CNPJ do sindicado ao qual o trabalhador encontra-se filiado |
| CfjSin | String(014) | Sim | CNPJ do sindicado ao qual o trabalhador encontra-se filiado |
| TipIea | Number(001,0) | Sim | Tipo de Inscrição do Empregador de Contratação Indireta do Aprendiz (CNPJ/CPF) |
| NumIea | Number(015,0) | Sim | Número da Inscrição do Contratante Indireto do Aprendiz |
| CfjIea | String(014) | Sim | Número da Inscrição do Contratante Indireto do Aprendiz |
| TetRgp | String(001) | Sim | Indicar se o servidor está sujeito ao teto do RGPS |
| IndAbo | String(001) | Sim | Indicar se o servidor recebe abono permanência |
| PanSeg | Number(002,0) | Sim | Tipo de plano de segregação da massa |
| CarEso | String(030) | Sim | Código do Cargo |
| DesCar | String(100) | Sim | Descrição do cargo |
| CodCbo | String(006) | Sim | Cbo 2002 do Cargo |
| IngSer | Date | Sim | Data do ingresso do servidor no cargo |
| CodFun | String(030) | Sim | Código da Função |
| DesFun | String(100) | Sim | Descrição da função |
| CboFun | String(006) | Sim | Cbo 2002 da Função |
| AcuCaF | String(001) | Sim | Indicar se cargo, emprego ou função pública é acumulável |
| MtvAlt | Number(002,0) | Sim | Motivo da alteração do cargo e/ou função |
| CodCat | Number(004,0) | Sim | Código da categoria |
| SalFix | Number(014,2) | Sim | Salário fixo do trabalhador |
| UndFix | Number(001,0) | Sim | Unidade de pagamento da parte fixa da remuneração |
| DesVar | String(999) | Sim | Descrição do salário variável e como este é calculado |
| TipCon | Number(001,0) | Sim | Tipo de contrato de trabalho |
| TerCon | Date | Sim | Data do Término do contrato |
| ObjDet | String(255) | Sim | Objetivo do término de contrato por prazo determinado |
| TInLoc | Number(001,0) | Sim | Tipo de inscrição do estabelecimento |
| NInLoc | String(014) | Sim | Número de inscrição do estabelecimento |
| DesLoc | String(080) | Sim | Descrição complementar do local de trabalho |
| LogDom | String(003) | Sim | Tipo de Logradouro - Doméstica |
| DesDom | String(100) | Sim | Descrição do logradouro - Doméstica |
| NumDom | String(010) | Sim | Número do logradouro - Doméstica |
| CplDom | String(030) | Sim | Complemento do logradouro - Doméstica |
| BaiDom | String(090) | Sim | Nome do bairro/distrito - Doméstica |
| CepDom | Number(008,0) | Sim | Código de Endereçamento Postal - Doméstica |
| MunDom | Number(007,0) | Sim | Código do município - Doméstica |
| EstDom | String(002) | Sim | Sigla da Unidade da Federação - Doméstica |
| HorSem | Number(004,2) | Sim | Quantidade média de horas relativas à jornada semanal do trabalhador |
| TipJor | Number(002,0) | Sim | Tipo de Jornada |
| VinCTP | Number(002,0) | Sim | Contrato a Tempo Parcial |
| HorNot | String(001) | Sim | Jornada semanal possui horário noturno (no todo ou em parte). |
| DesJor | String(999) | Sim | Descrição do tipo de jornada |
| JorTmp | String(001) | Sim | Contr. de trab. em regime de tempo parcial, cuja jornada não exceda 25 horas semanais |
| SinFil | Number(014,0) | Sim | CNPJ do sindicato ao qual o trabalhador encontra-se filiado (1) |
| CfjFil | String(014) | Sim | CNPJ do sindicato ao qual o trabalhador encontra-se filiado (1) |
| SinFi2 | Number(014,0) | Sim | CNPJ do sindicato ao qual o trabalhador encontra-se filiado (2) |
| CfjFi2 | String(014) | Sim | CNPJ do sindicato ao qual o trabalhador encontra-se filiado (2) |
| NumPro | String(021) | Sim | Número do processo judicial |
| JusCtr | String(999) | Sim | Justificativa da hipótese legal para a contratação de trabalho temporário |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| CodVin | Number(002,0) | Sim | Código do Vínculo |
| DatRef | Date | Sim | Data de Referência |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |
| IndCtr | Number(001,0) | Sim | Indicativo de Contratação |
| NumQua | Number(014,0) | Sim | CNPJ Entidade Qualificadora |
| CfjQua | String(014) | Sim | CNPJ Entidade Qualificadora |
| NumPra | Number(014,0) | Sim | CNPJ Atividades Práticas |
| CfjPra | String(014) | Sim | CNPJ Atividades Práticas |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqAco

---

## Índices

### R350ACOIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
